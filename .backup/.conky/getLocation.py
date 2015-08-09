
import urllib2
import urllib


def Get_UrlRespHtml(url):
    heads = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset':'GB2312,utf-8;q=0.7,*;q=0.7',
            'Accept-Language':'zh-cn,zh;q=0.5',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            #'Host':'John',
            'Keep-Alive':'115',
            'Referer':url,
            'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.14) Gecko/20110221 Ubuntu/10.10 (maverick) Firefox/3.6.14'}

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    opener.addheaders = heads.items()
    respHtml = opener.open(req).read()
    try:
        return respHtml.decode('gbk').encode('utf-8')
    except:
        return respHtml

def GetoutFromString(s,f,n):
    #s=""
    i_1 = s.find(f) +len (f)
    i_2 = s.find(n,i_1)
    return s[i_1:i_2]
html = Get_UrlRespHtml(r'http://1111.ip138.com/ic.asp')
#print (GetoutFromString(html,'[' , ']') )
ip =GetoutFromString(html,'[' ,']')

first =u'\u6765\u81EA\uFF1A'.encode('utf-8') #
end =u'\u003C\u002F\u0063\u0065\u006E\u0074\u0065\u0072\u003E'.encode('utf-8')#
location = html[html.find(first)+len(first):]
location  = GetoutFromString(html,first,end)

length =(len(location)/2)
length +=2
#if len(location)%2 == 1 :length+=2
print ( location +" | "+ip+" "*length)
