# coding:utf-8
import urllib2, re


def getlinks(data):
    realLink = ''
    HTMLString = ''
    if data != None:
        try:
            link = re.search("(?P<url>https?://[^\s]+)", data).group("url")
            if link is not None:
                request = urllib2.Request(link)
                request.add_header("user-agent", "Mozilla/5.0")
                response = urllib2.urlopen(request)
                realLink = response.url
                HTMLString = response.read()
                return realLink, HTMLString

        except:
            pass
