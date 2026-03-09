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
