from tkinter import *

# --- Window ---
window = Tk()
window.title("Camp Details Form")
window.state("zoomed")

camp_list = []

# --- Functions ---
def append_details():
    details = {
        "Row": entry_row.get(),
        "Location": entry_location.get(),
        "First Name": entry_first.get(),
        "Last Name": entry_last.get(),
        "Leader": entry_leader.get(),
        "Campers": entry_campers.get(),
        "Weather": entry_weather.get()
    }

    if all(details.values()):
        formatted = (
            f"Row {details['Row']} | {details['Location']} | "
            f"{details['First Name']} {details['Last Name']} | "
            f"Leader: {details['Leader']} | "
            f"Campers: {details['Campers']} | "
            f"Weather: {details['Weather']}"
        )

        camp_list.append(formatted)
        listbox.insert(END, formatted)

        for entry in entries:
            entry.delete(0, END)

def print_details():
    print("\nCamp Details:")
    for item in camp_list:
        print(item)

def quit_program():
    window.destroy()

# --- Labels ---
Label(window, text="Row").grid(row=0, column=0, padx=10, pady=10, sticky=E)
Label(window, text="Location").grid(row=0, column=2, padx=10, pady=10, sticky=E)

Label(window, text="First Name").grid(row=1, column=0, padx=10, pady=10, sticky=E)
Label(window, text="Last Name").grid(row=1, column=2, padx=10, pady=10, sticky=E)

Label(window, text="Leader").grid(row=2, column=0, padx=10, pady=10, sticky=E)
Label(window, text="Number of Campers").grid(row=2, column=2, padx=10, pady=10, sticky=E)

Label(window, text="Weather").grid(row=3, column=0, padx=10, pady=10, sticky=E)

# --- Entry Boxes ---
entry_row = Entry(window, width=25)
entry_row.grid(row=0, column=1, padx=10)

entry_location = Entry(window, width=25)
entry_location.grid(row=0, column=3, padx=10)

entry_first = Entry(window, width=25)
entry_first.grid(row=1, column=1, padx=10)

entry_last = Entry(window, width=25)
entry_last.grid(row=1, column=3, padx=10)

entry_leader = Entry(window, width=25)
entry_leader.grid(row=2, column=1, padx=10)

entry_campers = Entry(window, width=25)
entry_campers.grid(row=2, column=3, padx=10)

entry_weather = Entry(window, width=25)
entry_weather.grid(row=3, column=1, padx=10)

entries = [
    entry_row, entry_location, entry_first,
    entry_last, entry_leader, entry_campers,
    entry_weather
]

# --- Buttons ---
Button(window, text="Append Details", width=20, command=append_details)\
    .grid(row=4, column=0, columnspan=2, pady=20)

Button(window, text="Print Details", width=20, command=print_details)\
    .grid(row=4, column=2, columnspan=2)

Button(window, text="Quit", width=45, command=quit_program)\
    .grid(row=5, column=0, columnspan=4, pady=10)

# --- Listbox ---
listbox = Listbox(window, width=120, height=10)
listbox.grid(row=6, column=0, columnspan=4, padx=20, pady=20)

window.mainloop()