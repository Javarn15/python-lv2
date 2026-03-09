import tkinter as tk
from tkinter import messagebox

WINDOW_TITLE = "Julie's Party Hire"

#lists to store data 

customer_names = []
receipts_numbers= []
quantities = []
return_dates=[]

# ---------------- VALIDATION FUNCTION ----------------
def check_input(name, receipt, item, quantity, return_date):
    # check empty fields
    if name == "" or receipt == "" or item == "" or quantity == "" or return_date == "":
        messagebox.showerror("Input Error", "All fields must be filled in")
        return False
 
     # check quantity is a number
    if not quantity.isdigit():
        messagebox.showerror("Input Error", "Quantity must be a number")
        return False

    return True


# ---------------- ADD RECORD FUNCTION ----------------
def add_record():
    name = name_entry.get()
    receipt = receipt_entry.get()
    item = item_entry.get()
    quantity = quantity_entry.get()
    return_date = return_entry.get()

       # validate user input
    if check_input(name, receipt, item, quantity, return_date):
        
       # add data to lists
        customer_names.append(name)
        receipt_numbers.append(receipt)
        items_hired.append(item)
        quantities.append(quantity)
        return_dates.append(return_date)

        update_display()
        clear_inputs()
        

        # ---------------- UPDATE DISPLAY FUNCTION ----------------
def update_display():
    listbox.delete(0, tk.END)

    for i in range(len(customer_names)):
        record = customer_names[i] + " | " + items_hired[i] + " | Qty: " + quantities[i] + " | Return: " + return_dates[i]
        listbox.insert(tk.END, record)
 


 # ---------------- DELETE RECORD FUNCTION ----------------
def delete_record():
    selected = listbox.curselection()

    if selected:
        index = selected[0]

        customer_names.pop(index)
        receipt_numbers.pop(index)
        items_hired.pop(index)
        quantities.pop(index)
        return_dates.pop(index)

        update_display()
    else:
        messagebox.showerror("Selection Error", "Please select a record to delete")

