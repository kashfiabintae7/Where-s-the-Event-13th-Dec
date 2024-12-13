from tkinter import *

def conv_cm():
    
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text = f"{inches} inches = {cm: .2f} cm")
    
root = Tk()
root.title("Inches-->Centimeters Converter")
root.geometry("400x400")


ins_label = Label(root, text = "Enter Length in Inches: ", bg = "#936475", font = ("ATC Oak", 12))
ins_label.pack(pady = 10)

entry = Entry(root, width = 20, bg = "#bea8af", font = ("ATC Oak", 12))
entry.pack(pady = 5)

conv_button = Button(root, text = "Convert", command = conv_cm, bg = "#d299ad", fg = "white")
font = ("ATC Oak", 12)
conv_button.pack(pady = 10)

result_label = Label(root, text= "", font = ("ATC Oak", 14), fg = "white")
result_label.pack(pady = 10)

root.mainloop()