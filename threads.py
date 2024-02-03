import threading
import time


def function_A(semaphore_A, semaphore_B):
    for num in range(1, 6):
        semaphore_A.acquire()
        print(num)
        time.sleep(0.5)  
        semaphore_B.release()


def function_B(semaphore_A, semaphore_B):
    for letter in ['A', 'B', 'C', 'D', 'E']:
        semaphore_B.acquire()
        print(letter)
        time.sleep(0.5) 
        semaphore_A.release()


semaphore_A = threading.Semaphore(1)
semaphore_B = threading.Semaphore(0)


thread_A = threading.Thread(target=function_A, args=(semaphore_A, semaphore_B))
thread_B = threading.Thread(target=function_B, args=(semaphore_A, semaphore_B))


thread_A.start()
thread_B.start()


thread_A.join()
thread_B.join()


print("Program terminated.")
