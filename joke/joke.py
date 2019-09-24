import urllib.request
import urllib.parse
import re

rule_joke=re.compile('<span id=\"text110\">([\w\W]*?)</span>')
rule_url=re.compile('<a href=\"(.*?)\"target=\"_blank\" >')
mainUrl='http://www.jokeji.cn'
url='http://www.jokeji.cn/list.htm'

req=urllib.request.urlopen(url)
html=req.read().decode('gbk')
urls=rule_url.findall(html)
f=open('joke.txt','w')
for i in range(4):
    url2=urllib.parse.quote(urls[i])
    joke_url=mainUrl+url2
    req2=urllib.request.urlopen(joke_url)
    html2=req2.read().decode('gbk')
    joke=rule_joke.findall(html2)
    jokes=joke[0].split('<P>')
    
    for jokeStr in jokes:
        jokeStr=jokeStr.replace('</P>','')
        jokeStr=jokeStr.replace('<BR>','')
        jokeStr=jokeStr[2:]
        f.write(jokeStr)
f.close()