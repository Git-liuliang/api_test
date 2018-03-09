import time,json

def wrapper(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()

        res = {"ret": ret, "usetime": end - start}
        return res

    return inner

