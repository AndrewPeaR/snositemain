'''
Created on Mar 25, 2013

@author: user
'''
import Tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        bF = tk.Frame(self, bd=8, relief='sunken')
        bF.pack(expand='true', fill='x')

        var = tk.StringVar()
        var.set('Hello')
        entryLabel = tk.Label(self, textvariable=var)
        entryLabel.pack()

        mEntry = tk.Entry(self, bd=4, relief='sunken', textvariable=var)
        mEntry.pack()

gui = GUI()
gui.mainloop()