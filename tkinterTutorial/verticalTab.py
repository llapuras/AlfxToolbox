import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='ws')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')

f1 = tk.Frame(notebook, bg='red', width=200, height=200)
f2 = tk.Frame(notebook, bg='blue', width=200, height=200)
f3 = tk.Frame(notebook, bg='green', width=200, height=200)

notebook.add(f1, text='通道交换')
notebook.add(f2, text='格式转换')
notebook.add(f3, text='通道添加组合')
notebook.pack()

root.mainloop()
