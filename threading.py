import random
import time
import threading
def runner(name):
    for i in range(1,5):
        time.sleep(random.uniform(0.5,1.5))
        print(f"{name} ran step {i}")
    print(f"{name} finished the race!")
print("race is stared!")
thread1 = threading.Thread(target= runner, args=("Jimmy",))
thread2 = threading.Thread(target= runner, args=("Marlon",))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("race is over")