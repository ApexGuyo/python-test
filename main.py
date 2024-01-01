import tkinter
from tkinter import *
base = Tk()
base.geometry("500x500")
base.title("form")


fullname = Label(base, text="Full-name")
country = Label(base, text="country")

fullname.grid(row=1, column=2)
country.grid(row=2, column=2)

fullnamevalue = StringVar
countryvalue = StringVar

fullnameentry = Entry(base, textvariable=fullnamevalue)
countryentry = Entry(base, textvariable=countryvalue)

fullnameentry.grid(row=1, column=3)
countryentry.grid(row=2, column=3)

Button(base, text='Submit', width=20, bg='brown',
       fg='white').place(x=180, y=380)


base.mainloop()
