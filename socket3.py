import threading
import time

def sum(low, high):
    total =0
    count=0
    for i in range(low, high):
        total += i
    print("Subthread", total)
    while 1:
        count += 1
        time.sleep(5)
        print("\n\n서브 실행 중", count)

x=threading.Thread(target=sum, args=(1,10))
x.start()

def maintask():
    print("main task")
while 1:
    if input("메인 스레드 입력대기: "):
        maintask()
    time.sleep(0.2)