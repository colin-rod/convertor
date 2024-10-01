from tkinter import *

window = Tk()
window.title("Convertor")
window.minsize(width=500, height=300)

entry = Entry(width=10)
entry.focus_set()
entry.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(row=1, column=0)

label_km = Label(text="km")
label_km.grid(row=1, column=2)

label_converted_value = Label(text="0")
label_converted_value.grid(row=1, column=1)


def calculate():
    value = float(entry.get())
    converted_value = value * 1.609
    label_converted_value.config(text=f"{round(converted_value, 2)}")


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
