"SparkIdea  V1.1 - MainControl Part"  BIGDATA-PART will be upload in the future

For your qeustions:
1.a way to tell your project to start collecting tweets for certain keywords (rest api? or python rpc?)
please check the file:  SparkIdeaMain.py
this file will start a web application, in line 88 , there is a function "app@.route('/SparkIdeaInputKeyWords')" will open a HTML page for user and they can type the specific Key Words and News Source, and then it will start 2 Thread that transport the Keywords and NewsSource to BigDataPlatform(unitl now :2 Servers) and each server will start a Twitter collection program(same to file :BigData_NewsSourceInput.py).  

        
        
2.a way to get those tweets (e.g. the filtered tweets are simply stored in an sql database, or inverted control/event based API)

please check the file:  BigData_NewsSourceInput.py
this file show how to collect Twitter with specific KeyWord and NewsSource.
-"def StartMonitor(KeyWord, NewsSource):" this function can spcific the KeyWord And NewsSource(I put 30 newsSources as default selection)
-"class MyStreamer(TwythonStreamer):
        def on_success(self, data):"   this function can get the data from Twitter Server end
        
 
Pipeline:   

Until now 3 servers: A,B,C

Web Application (user input KeyWords ,server A) -> BigDataPlatform(server B and Server C) -> start collecting twitters and preprocessing the twitters(server B and Server C) -> write in a txt file(Server B , Server C) -> Flume read in(server B and Server C -> Server A) ->KafKa transport(Server A ,server B ,Server C) - >Spark parallel processing and counting(Server A ,server B ,Server C) -> store the MySQL DataBase(Server A)         Web Application show the results(search the MySQL DataBase every 1 second ,server A) (based on websock , long connection)


BIG PROBLEMES:


-when user open the web page and type input KeyWords, there is 2 threads will be started, even user close the web page, the threads doesn't stop!  and user can input Key Words many times and start many threads , this will be very dangerous!!!   How close old threds ,still not solve!

-Twitter streaming API  is endless, how can we stop it in program and open it again to change the key words?  

-when we stop the program how can we clean the data flow in Flume ,Kafka ,Spark? 

-Some strange Words or signs in Twitter can not recognise by Spark and will make it down.
