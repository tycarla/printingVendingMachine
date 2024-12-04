import tkinter as tk

def submit_form():
    name = name_var.get()
    date = date_var.get()
    panel = panel_var.get()
    print(f"Name: {name}, Date: {date}, Panel Members: {panel}")
    # Save or process input data

root = tk.Tk()
root.title("Fill in the Form")

tk.Label(root, text="Fill in the Form").grid(row=0, column=1, pady=10)

tk.Label(root, text="Name:").grid(row=1, column=0, sticky='w')
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).grid(row=1, column=1)

tk.Label(root, text="Date:").grid(row=2, column=0, sticky='w')
date_var = tk.StringVar()
tk.Entry(root, textvariable=date_var).grid(row=2, column=1)

tk.Label(root, text="Panel Members:").grid(row=3, column=0, sticky='w')
panel_var = tk.StringVar()
tk.Entry(root, textvariable=panel_var).grid(row=3, column=1)

tk.Button(root, text="Confirm Details", command=submit_form).grid(row=4, column=1, pady=20)

root.mainloop()
