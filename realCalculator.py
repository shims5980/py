import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Claculator")
        self.result_entry = tk.Entry(self.master, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, pady=10)
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "+"
        ]
        row_val = 1
        cal_val = 0
        for button_text in buttons:
            tk.Button(self.master, text=button_text, width=5, height=2, command=lambda btn=button_text: self.on_button_click(btn)).grid(row=row_val, column=cal_val, pady=5, padyx=5)
            cal_val += 1
            if cal_val > 3:
                cal_val = 0
                row_val += 1

        tk.Button(self.master, text='=', width=5, height=2, command=self.on_equals_button_click).grid(row=row_val, column=cal_val, pady=5, padx=5)
        tk.Button(self.master, text='C', width=5, height=2, command=self.on_delete_button_click).grid(row=row_val, column=cal_val+1, pady=5, padx=5)
        self.master.bind('<Return>', lambda event : self.on_equals_button_click())

        for i in range(10):
            key = str(i)
            self.master.bind(f'<Key>--{key}')


        def on_button_click(self, button_text, keysym=None):
            current_text = self.result_entry.get()
            print(keysym)
            if button_text == '=':
                try:
                    result = eval(current_text)
                    self.result_entry.delete(0, tk.END)
                    self.result_entry.insert(tk.END, str(result))
                except:
                    self.result_entry.delete(0, tk.END)
                    self.result_entry.insert(tk.END, "Error")
            else:
                if current_text == '0' or curren_text == "Error"


        def on_equals_button_click(self):
