import tkinter as tk
from tkinter import filedialog
import pandas as pd
from io import StringIO

class CSVEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("CSV Editor")
        self.load_button = tk.Button(self.master, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=10)
        self.text_box = tk.Text(self.master, height=10, width=50)
        self.text_box.pack(pady=10)
        self.save_button = tk.Button(self.master, text="Save Changes", command=self.save_chages)
        self.save_button.pack(pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path, encoding='cp949')
            except:
                self.df = pd.read_csv(file_path, encoding='utf-8')
            self.text_box.delete(0.0, tk.END)
            self.text_box.insert(tk.END, self.df.to_string(index=False))
    def save_chages(self):
        if hasattr(self, 'df'):
            edited_data = self.text_box.get("0.0", tk.END)
            edited_df = pd.read_csv(StringIO(edited_data))
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if file_path:
                edited_df.to_csv(file_path, index=False)
                tk.messagebox.showinfo("Success", "Change successfully")

root = tk.Tk()
csv_editor = CSVEditor(root)
root.mainloop()





