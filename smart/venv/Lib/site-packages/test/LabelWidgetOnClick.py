import Tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        bF = tk.Frame(self, bd=8, relief='sunken')
        bF.pack(expand='true', fill='x')
        changeButton = tk.Button(bF, text='Change', bd=4, fg='white',
                                relief='groove', activebackground='green',
                                command=self.change_label)
        changeButton.pack()

        self.entryLabel = tk.Label(self, text='Hello')
        self.entryLabel.pack()

        self.mEntry = tk.Entry(self, bd=4, relief='sunken')
        self.mEntry.pack()

    def change_label(self):
        data = self.mEntry.get()
        self.entryLabel.configure(text=data)


gui = GUI()
gui.mainloop()