import tkinter as tk
root = tk.Tk()
root.title("SIMPLE CALCULATOR")

root.geometry("450x400")
root.configure(bg="black")



#functions
def button_click(number):
    a = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(a) + str(number))
def button_clear():
    entry.delete(0, tk.END)
def button_equal():
    value = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, value)

#entry widget
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=15)

#buttons
buttons = [
    ("7", 1, 0, "grey"), ("8", 1, 1, "grey"), ("9", 1, 2, "grey"), ("/", 1, 3, "grey"),
    ("4", 2, 0, "grey"), ("5", 2, 1, "grey"), ("6", 2, 2, "grey"), ("*", 2, 3, "grey"),
    ("1", 3, 0, "grey"), ("2", 3, 1, "grey"), ("3", 3, 2, "grey"), ("-", 3, 3, "grey"),
    ("0", 4, 0, "grey"), ("C", 4, 1, "grey"), ("=", 4, 2, "grey"), ("+", 4, 0, "grey")
]
#loop for create and place button
for(text, row, col, color) in buttons:
    if text.isdigit() or text == ".":
        button = tk.Button(root, text=text, padx=40, pady=20, bg=color, command=lambda t=text: button_click(t))
    elif text == "C":
        button = tk.Button(root, text=text, padx=38, pady=20, bg=color, command=button_clear)
    elif text == "=":
        button = tk.Button(root, text=text, padx=50, pady=20, bg=color, command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=41, pady=20, bg=color, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5,  pady=5)

root.mainloop()