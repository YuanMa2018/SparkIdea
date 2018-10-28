<<<<<<< HEAD
import MySQLdb

class WeblogService:
    def queryWeblogs(self):
        titleNames = []
        titleCounts = []
        db = MySQLdb.connect("bigdata-pro01.yuanma.com", "root", "123456", "test", charset='utf8')
        cursor = db.cursor()
        sql = "select titleName,count from webCount where 1=1 order by count desc limit 30"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i, row in enumerate(results):
                titleNames.append(row[0])
                titleCounts.append(row[1])
                # print (titleNames[i], titleCounts[i])
            retMap = {'titleNames': titleNames, 'titleCounts': titleCounts};
            print(retMap)



            return retMap
        except:
            print "Error: unable to fecth data"
        db.close()

    def TotalTitleCount(self):
        db = MySQLdb.connect("bigdata-pro01.yuanma.com", "root", "123456", "test", charset='utf8')
        cursor = db.cursor()
        sql = "select count(1) titleSum from webCount"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print (results[0])
            return results[0]
        except:
            print "Error: unable to fecth data"
        db.close()

# w = WeblogService()
# w.queryWeblogs()
# w.TotalTitleCount()
=======
import MySQLdb

class WeblogService:
    def queryWeblogs(self):
        titleNames = []
        titleCounts = []
        db = MySQLdb.connect("bigdata-pro01.yuanma.com", "root", "123456", "test", charset='utf8')
        cursor = db.cursor()
        sql = "select titleName,count from webCount where 1=1 order by count desc limit 30"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for i, row in enumerate(results):
                titleNames.append(row[0])
                titleCounts.append(row[1])
                # print (titleNames[i], titleCounts[i])
            retMap = {'titleNames': titleNames, 'titleCounts': titleCounts};
            print(retMap)



            return retMap
        except:
            print "Error: unable to fecth data"
        db.close()

    def TotalTitleCount(self):
        db = MySQLdb.connect("bigdata-pro01.yuanma.com", "root", "123456", "test", charset='utf8')
        cursor = db.cursor()
        sql = "select count(1) titleSum from webCount"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print (results[0])
            return results[0]
        except:
            print "Error: unable to fecth data"
        db.close()

# w = WeblogService()
# w.queryWeblogs()
# w.TotalTitleCount()
>>>>>>> 6a9a1f8897db0d7c063476224d81cec9aa98e922
