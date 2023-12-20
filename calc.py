import tkinter
window = tkinter.Tk()
window.title("app")
window.geometry("640x480+100+100")
window.resizable(False, False)
def calc(event):
    label.config(text="결과="+str(eval(entry.get())))     # get은 조회 set은 설정, entry_get은 entry값을 가져옴

entry=tkinter.Entry(window)
entry.bind("<Return>", calc)    # <Return> 엔터를 의미 -> 엔터를 입력했을 때 calc 호출을 bind(할당)한다
entry.pack()
label=tkinter.Label(window, text='Label text default')
label.pack()
window.mainloop()
