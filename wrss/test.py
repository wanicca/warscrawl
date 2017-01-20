#coding=utf8
import os
import feedparser
import re
import webbrowser
import urllib2

def textProcess(s):
    pat1 = re.compile('</[^>]+>|<[^>]+/>')
    pat2 = re.compile('<[^>]+>')
    pat3 = re.compile('\n\n+')
    s = pat1.sub('\n',s)
    s = pat2.sub('',s)
    s = pat3.sub('\n\n',s)
    return s
def printTitle(n,s):
    print('\033[1;32;40m[%d]\033[1;31;40m%s\033[0m'%(n,s))
def openURL(url):
    webbrowser.open_new_tab(url)

def getHtml(url):
    html = urllib2.urlopen(url).read()
    return html

def saveHtml(file_name,file_content):
#    注意windows文件命名的禁用符，比如 /
    with open (file_name.replace('/','_')+".html","wb") as f:
#   写文件用bytes而不是str，所以要转码
        f.write( file_content )




print('加载配置中……')
if(not os.path.exists('linklist')):
    os.mknod('linklist')
listfile = open('linklist','r')
lklst = listfile.readlines()
showentmax = 5
showsummax = 200
print('每页%d条消息，每条消息展示前%d字'%(showentmax,showsummax))

for lk in lklst:
    print('当前来源：%s'%lk)
    feed = feedparser.parse(lk)
    print(feed.feed.title)
    count = 1
    for ent in feed.entries:
        # print ('\033[1;31;40m')
        # print (ent.title)
        # print ('\033[0m')
        printTitle((count-1)%showentmax+1,ent.title)
        if(len(ent.summary)<showsummax):
            print(textProcess(ent.summary))
        else:
            print (textProcess(ent.summary)[0:showsummax]+'\033[1;34m...(more)\033[0m')
        if(count%showentmax==0):
            print('-----(%d-%d)-----'%(count-showentmax,count))
            key = raw_input(">")
            while(key!=''):
                if(key[0]=='d'):
                    index=count-showentmax-1+int(key[1:])
                    html = getHtml(feed.entries[index].id)
                    saveHtml(feed.entries[index].title,html)
                    print ("缓存网页%d成功"%int(key[1:])) #下载文件
                else:
                    openURL(feed.entries[count-showentmax-1+int(key)].id) #打开外部浏览器
                key = raw_input(">")
        count+=1
