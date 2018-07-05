from multiprocessing import Process
import os
import datetime
import time
import sys
#Test Change Branch 1

def info(test_callback, title, time_wait):
    tmp = 5
    print(title+": "+title)
    test_callback(title, "f fun run")
    print(title+": "+str(datetime.datetime.now()))
    time.sleep(time_wait)
    print(title+": "+'time wait:', tmp)
    print(title+": "+'module name:', __name__)
    print(title+": "+'parent process:', os.getppid())
    print(title+": "+str(datetime.datetime.now()))
    print(title+": "+'process id:', os.getpid())
    tmp = 10


def f(title, name):
    print(title+": "+'hello', name)


def test1():
    current_module = f
    p = Process(target=info, args=(current_module, 'bob', 3,))
    r = Process(target=info, args=(current_module, 'rob', 5,))
    r.start()
    p.start()


def test2():
    current_module = f
    info(current_module, 'bob', 3,)
    info(current_module, 'rob', 5,)


if __name__ == '__main__':
    test2()
