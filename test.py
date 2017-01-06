import requests
import time

from cloudinsight import statsd

PM25_API_URL = "http://feed.aqicn.org/feed/%s/en/feed.v1.json"

def get_city_data(city):  
    try:
        res = requests.get(PM25_API_URL % city)
    except:
        return 0
    else:
        return res.json()['aqi']['val']

def using_sdk():  
    statsd.gauge('airquality.beijing.pm25', float(get_city_data('beijing')))
    statsd.gauge('airquality.wuhan.pm25', float(get_city_data('wuhan')))
    statsd.gauge('airquality.hefei.pm25', float(get_city_data('hefei')))

if __name__ == '__main__':  
    while 1 :
        using_sdk()
        time.sleep(5*60)

