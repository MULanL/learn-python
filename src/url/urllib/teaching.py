# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

def get_simple_urllib2():
    '''
    获取响应头和响应体信息
    '''
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get')
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

def get_params_urllib2():
    '''
    获取响应头和响应体信息
    '''
    params = urllib.urlencode({
        'param1': 'hello', 
        'param2': 'world',
        'author':'snowdreams1006',
        'website':'http://blog.snowdreams1006.cn',
        'url':'https://snowdreams1006.github.io/learn-python/url/urllib/teaching.html',
        'wechat':'snowdreams1006',
        'email':'snowdreams1006@163.com',
        'github':'https://github.com/snowdreams1006/'
    })
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/get?%s' % params)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

def post_params_urllib2():
    '''
    获取响应头和响应体信息
    '''
    params = urllib.urlencode({
        'param1': 'hello', 
        'param2': 'world',
        'author':'snowdreams1006',
        'website':'http://blog.snowdreams1006.cn',
        'url':'https://snowdreams1006.github.io/learn-python/url/urllib/teaching.html',
        'wechat':'snowdreams1006',
        'email':'snowdreams1006@163.com',
        'github':'https://github.com/snowdreams1006/'
    })
    response = urllib2.urlopen('http://httpbin.snowdreams1006.cn/post',params)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    print(response.read())

def get_proxy():
    '''
    获取随机代理
    '''
    response = urllib2.urlopen('http://proxyip.snowdreams1006.cn/get/')
    result = response.read()
    return json.loads(result)

def get_proxy_urllib():
    '''
    通过代理发送请求
    '''
    # 随机代理 ip
    ip = get_proxy().get('proxy')
    print('>>>Get Proxy:')
    print(ip)
    proxy = {
        'http': 'http://{}'.format(ip),
        'https': 'https://{}'.format(ip)
    }
    opener = urllib.FancyURLopener(proxy)
    response = opener.open("http://httpbin.snowdreams1006.cn/ip")
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    result = response.read()
    print(result)
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Set proxy success'
    else:
        print 'Set proxy fail'

def clear_proxy_urllib():
    '''
    清除代理后发送请求
    '''
    # 随机代理 ip
    ip = get_proxy().get('proxy')
    print('>>>Get Proxy:')
    print(ip)
    proxy = {
        'http': 'http://{}'.format(ip),
        'https': 'https://{}'.format(ip)
    }
    opener = urllib.FancyURLopener(proxy)
    response = opener.open("http://httpbin.snowdreams1006.cn/ip")
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    result = response.read()
    print(result)
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Set proxy success'
    else:
        print 'Set proxy fail'

    opener = urllib.FancyURLopener({})
    response = opener.open("http://httpbin.snowdreams1006.cn/ip")
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body:')
    result = response.read()
    print(result)
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Clear proxy fail'
    else:
        print 'Clear proxy success'

def send_proxy_urllib():
    '''
    通过代理获取响应头和响应体信息
    '''
    ip = get_proxy().get('proxy')
    print('>>>Get Proxy:')
    print(ip)
    proxies = {
        'http': 'http://{}'.format(ip),
        'https': 'https://{}'.format(ip)
    }
    response = urllib.urlopen('http://httpbin.snowdreams1006.cn/ip',proxies=proxies)
    result = response.read()
    result = json.loads(result)
    response_ip = result.get('origin')
    proxy_ip = ip.split(':')[0]
    if proxy_ip == response_ip:
        print 'Proxy Success'
    else:
        print 'Proxy Fail'

if __name__ == '__main__':
    print '>>>Get simple urllib2<<<'
    get_simple_urllib2()

    print '>>>Get params urllib2<<<'
    get_params_urllib2()

    print '>>>Post params urllib2<<<'
    post_params_urllib2()

    print '>>>Get proxy urllib<<<'
    get_proxy_urllib()

    print '>>>Clear proxy urllib<<<'
    clear_proxy_urllib()

    print '>>>Send proxy urllib<<<'
    send_proxy_urllib()
