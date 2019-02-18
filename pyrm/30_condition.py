import time
import threading


def consumer(cond):
    t = threading.currentThread()
    with cond:
        cond.wait()    # 等待满足条件
        print(f'{t.name}: Resource is available to consumer')


def producer(cond):
    t = threading.currentThread()
    with cond:
        print(f'{t.name}: Making resource available')
        cond.notifyAll()    # 唤醒消费者


condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=consumer, args=(condition,))

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()
