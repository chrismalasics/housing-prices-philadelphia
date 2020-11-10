#helpers for scraping

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


#********************    
#helpers for cleaning
#********************

#string to integer
def str_to_int(string):
    try:
        int(string)
        return int(string)
    except:
        return np.nan
    
#list to string
def list_to_str(x):
    x = x[2:-2]
    if len(x) > 0:
        return x
    else:
        return np.nan
    
#string to year   
def str_to_year(x):
    try:
        x = x[-4:]
        x = int(x)
        return x
    except:
        return np.nan
    
#zero to numpy NaN
def zero_to_nan(x):
    if x == 0:
        x == np.nan
        return x
    else:
        return x






