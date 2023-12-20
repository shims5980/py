import tkinter
window = tkinter.Tk()
window.title("app")
window.geometry("640x480+100+100")
window.resizable(False, False)

listbox = tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0, "1번")     # 특정 인덱스에 항목을 지정 (0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "2번")
listbox.insert(3, "2번")
listbox.insert(4, "3번")
listbox.pack()
listbox.activate(3)
print(listbox.get(0, 4))        # 인덱스 0~4까지 튜플 형태로 반환
print(listbox.size())
window.mainloop()