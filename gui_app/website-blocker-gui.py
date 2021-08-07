from tkinter import *
from tkinter import ttk


def block():
    pass



window = Tk()
window.title("Website Blocker")
window.geometry("1000x500")
window.config(bg="#32414b")


#
textToConvert = Text(window)
textToConvert.pack(fill = "none", expand = 1, side = "left")
textToConvert.config(bd = 0, padx = 6, pady = 15, font = ("Courier", 12), bg="#19232d", foreground="#99e66a", width = 40)
#
convertedText = Text(window)
convertedText.pack(fill = "none", expand = 1, side = "right")
convertedText.config(bd = 0, padx = 6, pady = 15, font = ("Courier", 12), bg="#19232d", foreground="#99e66a", width = 40)
# 
convert = Button(window, width = 10, bg = "#ffffff", fg = "#3775a9", text = "BLOCK", command = block)
convert.pack(fill = "none", expand = 1, side = "bottom")


window.mainloop()