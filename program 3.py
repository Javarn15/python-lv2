from tkinter import *

def quit():
    main_window.destroy()

def calculate_deck():

    Label (main_window, text="area").grid(column=0, row=4)
    deck_area = int(entry_deck_length.get()) * int(entry_deck_width.get())
    Label(main_window, text=deck_area).grid(column=1,row=4,sticky=W)


def main():
    Button(main_window , text="quit", command=quit) .grid(column=0, row=0)
    Button(main_window, text="calculate", command=calculate_deck) .grid(column=1, row=0)
    Label(main_window, text="length") .grid(column=0, row=1)
    Label(main_window, text="width") .grid(column=0, row=2)
    Label(main_window,text="height") .grid(column=0, row=3)
    main_window.mainloop()


main_window =Tk()
entry_deck_length = Entry(main_window)
entry_deck_length.grid(column=1,row=1,padx=10,pady=5)
entry_deck_width =Entry(main_window)
entry_deck_width.grid(column=1,row=2,padx=10,pady=5)
entry_deck_height =Entry(main_window)
entry_deck_height.grid(column=1,row=3,padx=10,pady=5)     


main()
