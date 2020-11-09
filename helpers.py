#helper functions

def get_proxy_list():
    from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
    proxies = []
    req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    proxies = req_proxy.get_proxy_list() #this will create proxy list

    proxies_address=[]
    for i in proxies:
        proxy = i.get_address()
        proxies_address.append(proxy)

    return list(set(proxies_address))

def format_proxy(ip_address):
    proxies = {'http': ip_address,
               'https': ip_address}
    return proxies

    
     