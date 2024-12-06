import tkinter as tk
from tkinter import ttk

def handle_button_click(clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        try:
            expression = current_text.replace("x", "*")
            result = eval(expression)

            if result.is_integer():
                result = int(result)
            
            result_var.set(result)
        except Exception:
            result_var.set("Error")
    elif clicked_button_text == "C":
        result_var.set("")
    elif clicked_button_text == "%":
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text == "±":
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_text + clicked_button_text)

def handle_key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.=":  
        handle_button_click(key)
    elif key == '\r':  # Enter
        handle_button_click("=")
    elif key == '\b':  # Backspace
        current_text = result_var.get()
        result_var.set(current_text[:-1])
    elif key == 'c':
         result_var.set("") 

root = tk.Tk()
root.title("Calculator")

root.configure(bg = "#212121")

result_var = tk.StringVar()
result_var_style = ttk.Style()

result_entry = ttk.Entry(root, textvariable=result_var, font=("Times New Roman", 24), justify="right", foreground="white")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
result_var_style.configure("default", background = "#212121") 

style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Times New Roman", 24), width=10, height=4, foreground = "white", background = "#212121")

result_entry_style = ttk.Style()
result_entry_style.configure("TEntry", fieldbackground="#212121", foreground="white", font=("Times New Roman", 24))

result_entry = ttk.Entry(
    root, 
    textvariable=result_var, 
    justify="right", 
    style="TEntry",
    font=("Times New Roman", 32)
)
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")


buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    button_style = ttk.Style()
    button_style.configure("TButton", foreground = "white", background = "#212121")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

for i in range(6):
    if(i == 0):
        root.grid_rowconfigure(i, weight=3)
        i += 1
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

width = 500
height = 700
root.geometry(f"{width}x{height}")

root.bind("<Key>", handle_key_press)
root.bind("<Return>", lambda event: handle_button_click("="))  # Enter
root.bind("<BackSpace>", lambda event: handle_key_press(event))  # Backspace

root.mainloop()
