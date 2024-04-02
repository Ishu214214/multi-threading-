import threading 
import os
import multiprocessing

def MYthread1(n):

    print(threading.current_thread().getName() +" " )
    print("ID of process running : " , os.getpid())
	
    print(n*n)
   




def cube(n):
    print(n*n*n)
    print(threading.current_thread().getName() +" " )
    print("ID of process running : " , os.getpid())





print("Main thread name: {}".format(threading.current_thread().name))
print("ID of process running : " , os.getpid())

# multi threading
t1=threading.Thread(target=MYthread1, args=[10])
t2=threading.Thread(target=cube,args=[10])
# multi processing
p1=multiprocessing.Process(target=cube, args= [5])


t1.start()
t2.start()

t1.join()
t2.join()

print()
print("multi processing")



p1.start()

p1.join()

