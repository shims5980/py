import tkinter

window = tkinter.Tk()

window.title("app")                             # 인터페이스 이름
window.geometry('640x400+100+100')              # 해상도 설정
window.resizable(False, False)     # 창크기 변경 가능여부

                     #window = 어디에 올릴 라벨인지                                         bd = 테두리두께
label = tkinter.Label(window, text="OCR", width=10, height=5, fg="red", relief="solid", bd=1)
#label = tkinter.Label(window, text="OCR")       # OCR 라벨의 크기만큼 ui의 크기로 할당됨
label.pack()

label1 = tkinter.Label(window, text="0")
count=0
def countUP():
    global count
    count += 1
    label1.config(text=str(count))
label1.pack()

# interval 주기를 갖고 반복, timeout 한번만 작동, repeatdelay 버튼을 누르고 있을 때 다음 버튼이 눌리는 딜레이
# repeatinterval 버튼을 계속 누르고 있을 때 다시 버튼이 반복되는 주기
button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()


# window ui 생성  메인루프는 무한으로 루프를 돌기에 코드 맨 아래에 위치
window.mainloop()

