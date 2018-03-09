import requests,json,random
from goods.utils import unitime
class Unicurl:
    """
    搜索api调用
    """
    def __init__(self,url,parms):
        """
        初始化相关数据,包括接口的url,headers和parm
        :return: None
        """
        self.url = url
        self.headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
        self.parms = parms

    @unitime.wrapper
    def get_data(self):
        """
        从接口获取数据
        :return:json,
        """
        wb_data = requests.get(self.url, headers=self.headers, params=self.parms)
        print(wb_data)
        print(type(wb_data))
        data = wb_data.json()
        if data['result'] == 0:
            retMsg = data['retMsg']
            result = data['responseInfo']
            return json.dumps(result)
        else:
            return json.dumps(data)


if __name__ == '__main__':

     tourl = 'http://172.18.11.112:8100/coomarts_home/search/getSearchGoods.htm'
     parms = {"keywords":"cpe","pageNum":1,"pageSize":6,"specialUser":True}
     uni = Unicurl(url=tourl,parms=parms)
     uni.get_data()
