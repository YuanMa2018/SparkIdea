from xmlrpclib import ServerProxy
import threading
# if __name__ == '__main__':
#     s = ServerProxy("http://192.168.2.151:49000")
#     print s.add(1,1)
#     print("no end")



# from xmlrpclib import ServerProxy
# if __name__ == '__main__':
#     s = ServerProxy("http://127.0.0.1:49000")
#     print s.StartMonitor()


def temp(x=1,y=1):
    s2 = ServerProxy("http://192.168.2.153:49000")
    s2.StartMonitor(x,y)
t2 = threading.Thread(target=temp, args=(1, 1))
t2.start()
print("start")

