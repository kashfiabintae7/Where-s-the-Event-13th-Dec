import tkinter as tk

def fahrenheit_to_celsius():
    
    fahrenheit = float(ent_temperature.get())
    celsius = (5/9) * (fahrenheit - 32)
    lbl_result["text"] = f"{round(celsius, 2)}\N{DEGREE CELSIUS}"
    
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width = False, height = False)
window.configure(bg = '#dac3a2')
                
frm_entry = tk.Frame(master = window)                 

ent_temperature = tk.Entry(master = frm_entry, width = 10)
lbl_temp = tk.Label(master = frm_entry, text = "\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row = 0, column = 0, sticky = "e")
lbl_temp.grid(row = 0, column = 1, sticky = "w")

btn_convert = tk.Button(master = window, text = "-->", command = fahrenheit_to_celsius, bg = "#9e855f")
lbl_result = tk.Label(master = window, text = "\N{DEGREE CELSIUS}")

frm_entry.grid(row = 0, column = 0, padx = 10)
btn_convert.grid(row = 0, column = 1, pady = 10)
lbl_result.grid(row = 0, column = 2, padx = 10)

window.mainloop()
