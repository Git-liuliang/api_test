import pymysql
from api_test import settings

class unisql:

    def __init__(self):
        self.host = settings.DATABASES["default"]["HOST"]
        self.user = settings.DATABASES["default"]["USER"]
        self.password = settings.DATABASES["default"]["PASSWORD"]
        self.database = settings.DATABASES["default"]["NAME"]


    def run(self,query):
        conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("excute >>",query,"make some error",e)
        finally:
            cursor.close()
            conn.close()
        try:
            return result
        except:
            print("no result")




if __name__ == '__main__':

    d = unisql()
    dd = d.run("select * from iskyshop_area where id = 300100 AND areaName = 'Boaco'")
    print(dd)


