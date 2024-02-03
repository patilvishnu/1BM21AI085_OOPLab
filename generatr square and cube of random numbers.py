import threading
import random
import time


shared_value = None
exit_flag = False
lock = threading.Lock()


def generate_random():
    global shared_value, exit_flag
    while not exit_flag:
        with lock:
            shared_value = random.randint(1, 100)
        time.sleep(1)


def compute_square():
    global shared_value, exit_flag
    while not exit_flag:
        with lock:
            if shared_value is not None and shared_value % 2 == 0:
                print(f"Square: {shared_value}^2 = {shared_value**2}")
        time.sleep(1)


def print_cube():
    global shared_value, exit_flag
    while not exit_flag:
        with lock:
            if shared_value is not None and shared_value % 2 != 0:
                print(f"Cube: {shared_value}^3 = {shared_value**3}")
        time.sleep(1)


thread1 = threading.Thread(target=generate_random)
thread2 = threading.Thread(target=compute_square)
thread3 = threading.Thread(target=print_cube)


thread1.start()
thread2.start()
thread3.start()


time.sleep(5)


exit_flag = True


thread1.join()
thread2.join()
thread3.join()
