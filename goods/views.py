from django.shortcuts import render,HttpResponse
import json
from goods import models
from goods.utils import commen,dbhelper
# Create your views here.
def test(request):
    '''
     1. url : need validate url
     2. keywords: need one more keywords like {"keywords":"cpe","pageNum":2}
     3. sql: need your sql to judge the data message
    :param request:
    :return:
    '''

    query = ""
    url = 'http://172.18.11.112:8100/coomarts_home/search/getSearchGoods.htm'
    parms = {"keywords": "cpe", "pageNum": 1, "pageSize": 6, "specialUser": True}


    uniq = dbhelper.unisql()
    # uniq.run(query)
    request_data = commen.Unicurl(url=url,parms=parms).get_data()
    print(type(request_data))
    print(request_data.get("ret"))
    res = json.loads(request_data.get("ret"))
    print(res.get("pageSize"))
    return  HttpResponse("ok")
