import tkinter as tk
from tkinter import messagebox, ttk

# ---------------- WINDOW ----------------
window = tk.Tk()
window.title("Julie's Party Hire System")
window.geometry("950x500")

# ---------------- LISTS ----------------
customer_names = []
receipt_numbers = []
items_hired = []
quantities = []
hired_date = []
return_dates = []

# ---------------- VALIDATION FUNCTION ----------------
def check_input(name, receipt, item_hired, quantity, hired_date, return_date):

    if name == "" or receipt == "" or items == "" or quantity == "" or hired_date == "" or return_date == "":
        messagebox.showerror("Input Error", "All fields must be filled in")
        return False

    # Name must be letters only
    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Input Error", "Customer full name must contain only letters")
        return False

    # Receipt number must be numbers only
    if not receipt.isdigit():
        messagebox.showerror("Input Error", "Receipt number must contain numbers only")
        return False

    # Item hired must be letters only
    if not item_hired.replace(" ", "").isalpha():
        messagebox.showerror("Input Error", "Item hired must contain letters only")
        return False

    # Quantity must be numbers only
    if not quantity.isdigit():
        messagebox.showerror("Input Error", "Quantity must be a number")
        return False
    

    if not hired_date.isdigit():
        messagebox.showerror("Input Error", "date hired must be a number")
        return False

    return True


# ---------------- APPEND DETAILS FUNCTION ----------------
def append_details():

    name = name_entry.get()
    receipt = receipt_entry.get()
    item = item_entry.get()
    quantity = quantity_entry.get()
    hired_date = hired_entry.get()
    return_date = return_entry.get()

    if check_input(name, receipt, item, quantity, hired_date, return_date):

        customer_names.append(name)
        receipt_numbers.append(receipt)
        items_hired.append(item)
        quantities.append(quantity)
        hired_date.append(hired_date)
        return_dates.append(return_date)

        clear_inputs()


# ---------------- PRINT DETAILS FUNCTION ----------------
def print_hire_details():

    for row in table.get_children():
        table.delete(row)

    for i in range(len(customer_names)):
        table.insert(
            "",
            "end",
            values=(
                i,
                customer_names[i],
                receipt_numbers[i],
                items_hired[i],
                quantities[i],
                hired_date[i],
                return_dates[i]
            )
        )


# ---------------- DELETE RETURNED ITEM ----------------
def delete_record():

    row_number = row_entry.get()

    if row_number == "":
        messagebox.showerror("Input Error", "Enter a row number")
        return

    if not row_number.isdigit():
        messagebox.showerror("Input Error", "Row must be a number")
        return

    index = int(row_number)

    if 0 <= index < len(customer_names):
        customer_names.pop(index)
        receipt_numbers.pop(index)
        items_hired.pop(index)
        quantities.pop(index)
        hired_date.pop(index)
        return_dates.pop(index)

        row_entry.delete(0, tk.END)
        print_hire_details()
    else:
        messagebox.showerror("Row Error", "That row does not exist")


# ---------------- CLEAR INPUT BOXES ----------------
def clear_inputs():

    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    hired_entry.delete(0, tk.END)
    return_entry.delete(0, tk.END)


# ---------------- QUIT PROGRAM ----------------
def quit_program():
    window.destroy()


# ---------------- LABELS ----------------
tk.Label(window, text="Customer Full Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Receipt Number").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Item Hired").grid(row=2, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Quantity").grid(row=3, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Hired Date").grid(row=4, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Return Date").grid(row=5, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Row").grid(row=6, column=0, padx=10, pady=10, sticky="w")

# ---------------- ENTRY BOXES ----------------
name_entry = tk.Entry(window, width=30)
name_entry.grid(row=0, column=1)

receipt_entry = tk.Entry(window, width=30)
receipt_entry.grid(row=1, column=1)

item_entry = tk.Entry(window, width=30)
item_entry.grid(row=2, column=1)

quantity_entry = tk.Entry(window, width=30)
quantity_entry.grid(row=3, column=1)

hired_entry = tk.Entry(window, width=30)
hired_entry.grid(row=4, column=1)

return_entry = tk.Entry(window, width=30)
return_entry.grid(row=5, column=1)

row_entry = tk.Entry(window, width=30)
row_entry.grid(row=6, column=1)

# ---------------- BUTTONS ----------------
tk.Button(window, text="Append Hire Details", width=20, command=append_details).grid(row=0, column=3, padx=20)
tk.Button(window, text="Print Hire Details", width=20, command=print_hire_details).grid(row=1, column=3, padx=20)
tk.Button(window, text="Row to delete  ", width=20, command=delete_record).grid(row=2, column=3, padx=20)
tk.Button(window, text="Quit Program", width=20, command=quit_program).grid(row=3, column=3, padx=20)

# ---------------- TABLE DISPLAY ----------------
table = ttk.Treeview(
    window,
    columns=("id", "name", "receipt", "item", "qty", "hired", "return"),
    show="headings",
    height=10
)

table.heading("id", text="#")
table.heading("name", text="Customer Name")
table.heading("receipt", text="Receipt Number")
table.heading("item", text="Item Hired")
table.heading("qty", text="Quantity")
table.heading("hired", text="Hired Date")
table.heading("return", text="Return Date")

table.column("id", width=40, anchor="center")
table.column("name", width=180)
table.column("receipt", width=120, anchor="center")
table.column("item", width=140)
table.column("qty", width=80, anchor="center")
table.column("hired", width=120, anchor="center")
table.column("return", width=120, anchor="center")

table.grid(row=7, column=0, columnspan=4, padx=10, pady=30)

# ---------------- RUN PROGRAM ----------------
window.mainloop()