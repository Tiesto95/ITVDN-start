import time
from functools import wraps

def time_decor(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        time_result = time.time()
        func(*args, **kwargs)
        print(time.time() - time_result)

    return wrap


@time_decor
def test(sleep):
    time.sleep(sleep)


test(sleep=5)
