import tkinter as tk
from tkinter import messagebox

# --- Sample data ---
data = [
    ["Jim", "Sandy Beach", 6, "Cold"],
    ["Jake", "Hilltop", 9, "Snow"],
    ["Jilly", "Valley Flat", 7, "Sunny"]
]

# --- Functions ---
def show(i=0):
    if data:
        for j in range(len(vars)):
            vars[j].set(data[i][j])
        entry_row.config(state="normal")
        entry_row.delete(0, tk.END)
        entry_row.insert(0, str(i))
        entry_row.config(state="readonly")
    else:
        for v in vars:
            v.set("")

def append_details():
    record = [v.get() for v in vars[:-1]]  # exclude row #
    if all(record):
        data.append(record)
        messagebox.showinfo("Added", "Record added")
        show(len(data)-1)
    else:
        messagebox.showwarning("Warning", "Please fill all fields")

def delete():
    if data:
        row_index = int(entry_row.get())
        data.pop(row_index)
        messagebox.showinfo("Deleted", f"Record {row_index} deleted")
        show(0)
    else:
        messagebox.showwarning("Warning", "No records to delete")

def print_details():
    print("\nCamping Records:")
    for i, record in enumerate(data):
        print(f"{i}: {record}")

# --- Main Window ---
root = tk.Tk()
root.title("Camping Records")
root.geometry("600x250")

# --- Frames ---
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# --- Labels and Entry Boxes ---
labels = ["Leader", "Location", "No of Campers", "Weather", "Row #"]
vars = [tk.StringVar() for _ in labels[:-1]]  # Last one is row #
entries = []

for i, text in enumerate(labels[:-1]):
    tk.Label(frame_inputs, text=text, font=("Arial", 10)).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(frame_inputs, textvariable=vars[i], width=25)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Row # entry (readonly)
tk.Label(frame_inputs, text=labels[-1], font=("Arial", 10)).grid(row=len(labels)-1, column=0, padx=5, pady=5, sticky="e")
entry_row = tk.Entry(frame_inputs, width=10, justify="center", state="readonly")
entry_row.grid(row=len(labels)-1, column=1, padx=5, pady=5, sticky="w")

# --- Buttons ---
tk.Button(frame_buttons, text="Append Details", width=15, command=append_details).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Delete", width=15, command=delete).grid(row=0, column=1, padx=10)
tk.Button(frame_buttons, text="Print Details", width=15, command=print_details).grid(row=0, column=2, padx=10)
tk.Button(frame_buttons, text="Quit", width=15, command=root.quit).grid(row=0, column=3, padx=10)

# --- Show first record ---
show()

root.mainloop()