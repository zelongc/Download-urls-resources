
import urllib.request
import socket
import threading
import queue

import os


myqueue=queue.Queue()

socket.setdefaulttimeout(5.0)
global count
count =0

lock=threading.Lock()

# read file that contains urls,
def read_file():
    with open('/Users/nick/Dropbox/Python/Python Workplace/Tools/worker_url.txt', 'r') as reader:
        for each in reader.readlines():
            myqueue.put(each)
    return myqueue
# dowload and name it:

def download(url):
    try:
        global count
        urllib.request.urlretrieve(url,'/Users/nick/Dropbox/Python/Python Workplace/Tools/pic/pic_'+'%s.jpg' % count)
    except:
        print("error")
        return 0
    print("pic "+count.__str__()+" finished")
    print("downloaded "+url)
    lock.acquire(True)
    try :

        count=count+1
    finally:
        lock.release()

def run():
    while myqueue.not_empty:
        download(myqueue.get())

def main():
    myqueue=read_file()

    print("finish reading the file")
    t1=threading.Thread(target=run)
    t2=threading.Thread(target=run)
    t3=threading.Thread(target=run)
    t1.run()
    t2.run()
    t3.run()
if __name__ == '__main__':
    main()
