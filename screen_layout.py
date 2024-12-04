import tkinter as tk

def confirm_selection():
    selected = form_var.get()
    if selected:
        print(f"Form Selected: {selected}")
        # Proceed to next step (user input)
    else:
        print("No form selected!")

root = tk.Tk()
root.title("Form Selection")

form_var = tk.StringVar()

tk.Label(root, text="Select a Form").pack(pady=10)

tk.Radiobutton(root, text="Oral Presentation and Billing Form", variable=form_var, value="Oral Presentation").pack(anchor='w')
tk.Radiobutton(root, text="Rubric for Design and Thesis", variable=form_var, value="Rubric").pack(anchor='w')
tk.Radiobutton(root, text="Recommendation Form", variable=form_var, value="Recommendation").pack(anchor='w')

tk.Button(root, text="Next", command=confirm_selection).pack(pady=20)

root.mainloop()
