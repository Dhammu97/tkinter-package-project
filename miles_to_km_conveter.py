from tkinter import *

win = Tk()
win.title("Mile to Kilometer Converter")
# win.minsize(width=500, height=500)
win.config(padx=50, pady=50)

entry = Entry()
entry.grid(column=1, row=0)
entry.config()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

convert_to_km = Label(text="Convert to Km")
convert_to_km.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

km = Label(text="KM")
km.grid(column=2, row=1)


def calculate_km():
    miles = entry.get()
    converter = float(miles) * 1.609
    km_label.config(text=converter)


button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

win.mainloop()
