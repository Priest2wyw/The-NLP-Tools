from multiprocessing import Pool
import os, time, random
import time

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def Fibonacci(n):
    if n <=2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) 

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(16)
    for i in range(17):
        p.map_async(Fibonacci, (42,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


    # for i  in range(100):
    #     a =time.time()
    #     print(i,Fibonacci(i))
    #     b = time.time()

    #     print('共用时',b-a,'秒。')