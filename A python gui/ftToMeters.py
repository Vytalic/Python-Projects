from tkinter import *
from tkinter import ttk

def calculateFeet(*args):                                               # Converting ft
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)         # ft to meters
        inches.set(int(12 * value))                                     # ft to inches
        centimeters.set(int(0.3048 * value * 10000.0 + 0.5)/100.0)      # ft to cm
        feet_entry.focus()
        root.bind("<Return>", calculateFeet)
    except ValueError:
        pass
    
def calculateMeters(*args):                         # Converting meters
    try:
        value = float(meters.get())
        feet.set(float(value * 3.28084))            # meters to ft
        inches.set(float(39.3701 * value))          # meters to inches
        centimeters.set(float(value * 100))         # meters to cm
        meters_entry.focus()
        root.bind("<Return>", calculateMeters)
    except ValueError:
        pass
    
def calculateInches(*args):                         # Converting inches
    try:
        value = float(inches.get())
        feet.set(float(value / 12))                 # inches to ft
        meters.set(float(value * 0.0254))           # inches to meters
        centimeters.set(float(value * 2.54))        # inches to cm
        inches_entry.focus()
        root.bind("<Return>", calculateInches)
    except ValueError:
        pass
    
def calculateCentimeters(*args):                    # Converting cm
    try:
        value = float(centimeters.get())
        feet.set(float(value * 0.0328084))          # cm to ft
        inches.set(float(0.393701 * value))         # cm to inches
        meters.set(float(value / 100))              # cm to meters
        centimeters_entry.focus()
        root.bind("<Return>", calculateCentimeters)
    except ValueError:
        pass


root = Tk()
root.title("Conversion Sheet")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
meters_entry = ttk.Entry(mainframe, width=7, textvariable=meters)
meters_entry.grid(column=2, row =2, sticky=(W, E))

inches = StringVar()
inches_entry = ttk.Entry(mainframe, width=7, textvariable=inches)
inches_entry.grid(column=2, row =3, sticky=(W, E))

centimeters = StringVar()
centimeters_entry = ttk.Entry(mainframe, width=7, textvariable=centimeters)
centimeters_entry.grid(column=2, row =4, sticky=(W, E))


ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculateFeet).grid(column=4, row=1, sticky=W)

ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculateMeters).grid(column=4, row=2, sticky=W)

ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="inches").grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculateInches).grid(column=4, row=3, sticky=W)

ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="centimeters").grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculateCentimeters).grid(column=4, row=4, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)



root.mainloop()