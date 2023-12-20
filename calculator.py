import tkinter as tk
window=tk.Tk()

class calculator:
    menu = -1
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("640x480+100+100")
        self.master.resizable(False, False)
        self.text_box = tk.Text(self.master, height=3, width=53)
        self.text_box.pack(pady=10)

        # 1~0까지 숫자 버튼
        self.bt1 = tk.Button(self.master, text="1", command=self.one, width=10, height=3)
        self.bt1.place(x=150, y=70)
        self.bt2 = tk.Button(self.master, text="2", command=self.two, width=10, height=3)
        self.bt2.place(x=280, y=70)
        self.bt3 = tk.Button(self.master, text="3", command=self.three, width=10, height=3)
        self.bt3.place(x=410, y=70)
        self.bt4 = tk.Button(self.master, text="4", command=self.four, width=10, height=3)
        self.bt4.place(x=150, y=170)
        self.bt5 = tk.Button(self.master, text="5", command=self.five, width=10, height=3)
        self.bt5.place(x=280, y=170)
        self.bt6 = tk.Button(self.master, text="6", command=self.six, width=10, height=3)
        self.bt6.place(x=410, y=170)
        self.bt7 = tk.Button(self.master, text="7", command=self.seven, width=10, height=3)
        self.bt7.place(x=150, y=270)
        self.bt8 = tk.Button(self.master, text="8", command=self.eight, width=10, height=3)
        self.bt8.place(x=280, y=270)
        self.bt9 = tk.Button(self.master, text="9", command=self.nine, width=10, height=3)
        self.bt9.place(x=410, y=270)
        self.bt0 = tk.Button(self.master, text="0", command=self.zero, width=10, height=3)
        self.bt0.place(x=280, y=370)

        # 초기화, 결과, 사칙연산 버튼
        self.btc = tk.Button(self.master, text="C", command=self.dele, width=10, height=3)
        self.btc.place(x=150, y=470)
        self.btre = tk.Button(self.master, text="=", command=self.re, width=10, height=3)
        self.btre.place(x=410, y=470)


    def one(self):
        self.text_box.insert(tk.END, 1)
    def two(self):
        self.text_box.insert(tk.END, 2)
    def three(self):
        self.text_box.insert(tk.END, 3)
    def four(self):
        self.text_box.insert(tk.END, 4)
    def five(self):
        self.text_box.insert(tk.END, 5)
    def six(self):
        self.text_box.insert(tk.END, 6)
    def seven(self):
        self.text_box.insert(tk.END, 7)
    def eight(self):
        self.text_box.insert(tk.END, 8)
    def nine(self):
        self.text_box.insert(tk.END, 9)
    def zero(self):
        self.text_box.insert(tk.END, 0)
    def dele(self):
        self.text_box.delete(0.0, tk.END)
    def re(self):

root = tk.Tk()
calc = calculator(root)
root.mainloop()
