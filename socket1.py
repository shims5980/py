import socket
from threading import Thread
import tkinter

tk = tkinter.Tk()
tk.geometry("1000x1000")
entry = tkinter.Entry(tk)
entry2 = tkinter.Listbox(tk, height = 15, width = 50)
#HOST = '192.168.214.51'
HOST = '192.168.214.24'
#HOST = '172.29.183.1'
PORT = 9900

def rcvMsg(sock):
    while True:
        try:
            data=sock.recv(1024)
            if not data:
                break
            print(data.decode())
            entry2.insert(-1, data.decode() + "\n")
            entry2.update()
            entry2.see(0)
        except:
            pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:     # with 이용해 파일 오픈, as 뒤에는 식별자
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg, args=(sock,))         # 쓰레드 안 argument로 보내기 위해선 1개 더라도 튜플 형태로 보내야함
        t.daemon = True     # 데몬스레드로 설정해서 메인 스레드가 종료되면 자동으로 같이 종료 / 프로세스 묶이는 문제 방지
        t.start()

        def okClick():
            sock.send(entry.get().encode())         # 엔트리 입력된 데이터 방트 단위로 바꿈 ->.encode()
        def onEnter():
            okClick()
            entry.delete(0, tkinter.END)

        entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
        label = tkinter.Label(tk, text="채팅")
        entry.pack()
        label.pack()
        btn = tkinter.Button(tk, text="OK", command=okClick)
        btn.pack()
        entry.bind("<Return>", onEnter)
        tk.mainloop()
runChat()