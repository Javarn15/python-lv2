import tkinter as tk
from tkinter import messagebox, ttk   # imports GUI tools and message boxes for user interaction

# ---------------- CONSTANTS ----------------
# These values are fixed and used throughout the program instead of hardcoding numbers
WINDOW_WIDTH = 950
WINDOW_HEIGHT = 500
ENTRY_WIDTH = 30
BUTTON_WIDTH = 20
TABLE_HEIGHT = 10
ID_COLUMN_WIDTH = 40
NAME_COLUMN_WIDTH = 180
RECEIPT_COLUMN_WIDTH = 120
ITEM_COLUMN_WIDTH = 140
QTY_COLUMN_WIDTH = 80
DATE_COLUMN_WIDTH = 120

# ---------------- WINDOW ----------------
# Creates the main application window and sets its title and size
window = tk.Tk()
window.title("Julie's Party Hire System")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# ---------------- LISTS ----------------
# These lists store all customer hire information (each index represents one record)
customer_names = []
receipt_numbers = []
items_hired = []
quantities = []
hired_dates = []
return_dates = []

# ---------------- VALIDATION FUNCTION ----------------
# This function checks all user input and ensures it is valid before storing it
def check_input(name, receipt, item_hired, quantity, hired_date, return_date):

    # Checks that no fields are left empty
    if name == "" or receipt == "" or item_hired == "" or quantity == "" or hired_date == "" or return_date == "":
        messagebox.showerror("Input Error", "All fields must be filled in")
        return False

    # Ensures the customer name contains only letters (no numbers or symbols)
    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Input Error", "Customer full name must contain only letters")
        return False

    # Ensures receipt number contains only digits
    if not receipt.isdigit():
        messagebox.showerror("Input Error", "Receipt number must contain numbers only")
        return False

    # Ensures item name only contains letters
    if not item_hired.replace(" ", "").isalpha():
        messagebox.showerror("Input Error", "Item hired must contain letters only")
        return False

    # Ensures quantity is a number
    if not quantity.isdigit():
        messagebox.showerror("Input Error", "Quantity must be a number")
        return False

    # Ensures hired date is in correct format DD/MM/YYYY
    if hired_date.count("/") != 2:
        messagebox.showerror("Input Error", "Hired date must be in DD/MM/YYYY format")
        return False

    hired_parts = hired_date.split("/")
    if len(hired_parts) != 3 or not all(part.isdigit() for part in hired_parts):
        messagebox.showerror("Input Error", "Hired date must be in DD/MM/YYYY format")
        return False

    # Checks correct length of day, month, and year
    day, month, year = hired_parts
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        messagebox.showerror("Input Error", "Hired date must be in DD/MM/YYYY format")
        return False

    # Ensures return date is in correct format DD/MM/YYYY
    if return_date.count("/") != 2:
        messagebox.showerror("Input Error", "Return date must be in DD/MM/YYYY format")
        return False

    return_parts = return_date.split("/")
    if len(return_parts) != 3 or not all(part.isdigit() for part in return_parts):
        messagebox.showerror("Input Error", "Return date must be in DD/MM/YYYY format")
        return False

    day, month, year = return_parts
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        messagebox.showerror("Input Error", "Return date must be in DD/MM/YYYY format")
        return False

    # If all checks pass, return True so the data can be added
    return True

# ---------------- APPEND DETAILS FUNCTION ----------------
# This function gets user input and stores it into the lists
def append_details():

    # Get values entered by the user from entry boxes
    name = name_entry.get()
    receipt = receipt_entry.get()
    item = item_entry.get()
    quantity = quantity_entry.get()
    hired = hired_entry.get()
    returned = return_entry.get()

    # Only store data if validation is successful
    if check_input(name, receipt, item, quantity, hired, returned):

        # Add each value to its corresponding list
        customer_names.append(name)
        receipt_numbers.append(receipt)
        items_hired.append(item)
        quantities.append(quantity)
        hired_dates.append(hired)
        return_dates.append(returned)

        # Clear input boxes after storing data
        clear_inputs()

# ---------------- PRINT DETAILS FUNCTION ----------------
# This function displays all stored records in the table
def print_hire_details():

    # Removes all existing rows from the table before updating
    for row in table.get_children():
        table.delete(row)

    # Loops through all stored records and inserts them into the table
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
                hired_dates[i],
                return_dates[i]
            )
        )

# ---------------- DELETE RETURNED ITEM ----------------
# This function deletes a selected record based on the row number entered
def delete_record():

    row_number = row_entry.get()

    # Checks if row input is empty
    if row_number == "":
        messagebox.showerror("Input Error", "Enter a row number")
        return

    # Ensures row number is numeric
    if not row_number.isdigit():
        messagebox.showerror("Input Error", "Row must be a number")
        return

    index = int(row_number)

    # Checks if the row exists in the list
    if 0 <= index < len(customer_names):
        # Removes the selected record from all lists
        customer_names.pop(index)
        receipt_numbers.pop(index)
        items_hired.pop(index)
        quantities.pop(index)
        hired_dates.pop(index)
        return_dates.pop(index)

        # Clears row input and updates table display
        row_entry.delete(0, tk.END)
        print_hire_details()
    else:
        messagebox.showerror("Row Error", "That row does not exist")

# ---------------- CLEAR INPUT BOXES ----------------
# This function clears all entry fields after data is added
def clear_inputs():

    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    hired_entry.delete(0, tk.END)
    return_entry.delete(0, tk.END)

# ---------------- QUIT PROGRAM ----------------
# This function closes the application window
def quit_program():
    window.destroy()

# ---------------- LABELS ----------------
# These labels describe each input field in the GUI
tk.Label(window, text="Customer Full Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Receipt Number").grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Item Hired").grid(row=2, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Quantity").grid(row=3, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Hired Date").grid(row=4, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Return Date").grid(row=5, column=0, padx=10, pady=10, sticky="w")
tk.Label(window, text="Row").grid(row=6, column=0, padx=10, pady=10, sticky="w")

# ---------------- ENTRY BOXES ----------------
# Entry boxes allow the user to type input data
name_entry = tk.Entry(window, width=ENTRY_WIDTH)
name_entry.grid(row=0, column=1)

receipt_entry = tk.Entry(window, width=ENTRY_WIDTH)
receipt_entry.grid(row=1, column=1)

item_entry = tk.Entry(window, width=ENTRY_WIDTH)
item_entry.grid(row=2, column=1)

quantity_entry = tk.Entry(window, width=ENTRY_WIDTH)
quantity_entry.grid(row=3, column=1)

hired_entry = tk.Entry(window, width=ENTRY_WIDTH)
hired_entry.grid(row=4, column=1)

return_entry = tk.Entry(window, width=ENTRY_WIDTH)
return_entry.grid(row=5, column=1)

row_entry = tk.Entry(window, width=ENTRY_WIDTH)
row_entry.grid(row=6, column=1)

# ---------------- BUTTONS ----------------
# Buttons trigger functions when clicked by the user
tk.Button(window, text="Append Hire Details", width=BUTTON_WIDTH, command=append_details).grid(row=0, column=3, padx=20)
tk.Button(window, text="Print Hire Details", width=BUTTON_WIDTH, command=print_hire_details).grid(row=1, column=3, padx=20)
tk.Button(window, text="Row to Delete", width=BUTTON_WIDTH, command=delete_record).grid(row=2, column=3, padx=20)
tk.Button(window, text="Quit Program", width=BUTTON_WIDTH, command=quit_program).grid(row=3, column=3, padx=20)

# ---------------- TABLE DISPLAY ----------------
# This table displays all stored hire records in a structured format
table = ttk.Treeview(
    window,
    columns=("id", "name", "receipt", "item", "qty", "hired", "return"),
    show="headings",
    height=TABLE_HEIGHT
)

# Sets headings for each column
table.heading("id", text="#")
table.heading("name", text="Customer Name")
table.heading("receipt", text="Receipt Number")
table.heading("item", text="Item Hired")
table.heading("qty", text="Quantity")
table.heading("hired", text="Hired Date")
table.heading("return", text="Return Date")

# Sets width and alignment of each column
table.column("id", width=ID_COLUMN_WIDTH, anchor="center")
table.column("name", width=NAME_COLUMN_WIDTH)
table.column("receipt", width=RECEIPT_COLUMN_WIDTH, anchor="center")
table.column("item", width=ITEM_COLUMN_WIDTH)
table.column("qty", width=QTY_COLUMN_WIDTH, anchor="center")
table.column("hired", width=DATE_COLUMN_WIDTH, anchor="center")
table.column("return", width=DATE_COLUMN_WIDTH, anchor="center")

# Places the table in the window
table.grid(row=7, column=0, columnspan=4, padx=10, pady=30)

# ---------------- RUN PROGRAM ----------------
# Starts the GUI program loop so the window stays open and responds to user actions
window.mainloop()