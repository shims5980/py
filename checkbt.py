import tkinter
window = tkinter.Tk()
window.title("app")
window.geometry("640x480+100+100")
window.resizable(False, False)

'''
def flash():
    checkbutton1.flash()

def desel():
    checkbutton1.deselect()     # 체크 해제
    checkbutton2.deselect()
    checkbutton3.deselect()


CheckVariety_1=tkinter.IntVar()     # x = 10처럼 직접 대입하면 안되고 정수변수를 선언해줘야한다.
CheckVariety_2=tkinter.IntVar()     # 문자 변수는 tkinter.StringVar()
CheckVariety_3=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="0", variable=CheckVariety_1, activebackground="blue")
checkbutton2=tkinter.Checkbutton(window, text="△", variable=CheckVariety_2, command=desel)
checkbutton3=tkinter.Checkbutton(window, text="ㅁ", variable=CheckVariety_3, command=flash)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
'''

'''
def flash():
    checkbutton1.flash()
    CheckVariety_2.set("flash")
    checkbutton1.config(text=CheckVariety_2.get())

CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.StringVar()

checkbutton1=tkinter.Checkbutton(window, text="0", variable=CheckVariety_1, activebackground="blue")
checkbutton3=tkinter.Checkbutton(window, text="ㅁ", variable=CheckVariety_2, command=flash)

checkbutton1.pack()
checkbutton3.pack()
'''

'''
def flash():
    checkbutton1.flash()
    checkbutton1.config(text=CheckVariety_2.get())

CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="0", variable=CheckVariety_1, activebackground="blue")
checkbutton3=tkinter.Checkbutton(window, text="ㅁ", variable=CheckVariety_2, command=flash)

checkbutton1.pack(side='left', padx=50)     # padx(padding x) x축 50만큼의 너비를 줌
checkbutton3.pack(side='left')
'''

'''
b1=tkinter.Button(window, text="top")
b1_1=tkinter.Button(window, text="top-1")
b2=tkinter.Button(window, text="bottom")
b2_1=tkinter.Button(window, text="bottom-1")
b3=tkinter.Button(window, text="left")
b3_1=tkinter.Button(window, text="left-1")
b4=tkinter.Button(window, text="right")
b4_1=tkinter.Button(window, text="right-1")
b5=tkinter.Button(window, text="center", bg="red")

b1.pack(side="top")
b1_1.pack(side="top", fill="x")
b2.pack(side="bottom")
b2_1.pack(side="bottom", anchor="e")
b3.pack(side="left")
b3_1.pack(side="left", fill="y")
b4.pack(side="right")
b4_1.pack(side="right", anchor="s")
b5.pack(expand=True, fill="both")
'''

b1=tkinter.Button(window, text="(50, 50)")
b2=tkinter.Button(window, text="[50, 100)")
b3=tkinter.Button(window, text="(100, 150)")
b4=tkinter.Button(window, text="(0, 200)")
b5=tkinter.Button(window, text="(0, 300)")
b6=tkinter.Button(window, text="(0, 300)")
b1.place(x=50, y=50)
b2.place(x=50, y=100, width=50, height=50)
b3.place(x=100, y=150, bordermode="inside")
b4.place(x=0, y=200, relwidth=0.5)
b5.place(x=0, y=300, relx=0.5)
b6.place(x=0, y=300, relx=0.5, anchor="s")


#set get eval entry button command IntVar StringVar Label listbox

window.mainloop()