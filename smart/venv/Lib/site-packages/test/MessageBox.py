import Tkinter as tki # Tkinter -> tkinter in Python 3

class GUI(tki.Tk):
    def __init__(self):
        tki.Tk.__init__(self)
        self.username = 'Bob' # a default name

        button0 = tki.Button(self, text='Set user', command=self.msg_box)
        button0.pack()

        # notice that lambda allows us to pass args
        button1 = tki.Button(self, text='Show user', command=lambda: self.msg_box(value, False))
        button1.pack()

    def msg_box(self, msg='User name?', extra=True):
        top = self.top = tki.Toplevel(self)
        label0 = tki.Label(top, text=msg)
        label0.pack()

        if extra:
            self.entry0 = tki.Entry(top)
            self.entry0.pack()

            button2 = tki.Button(top, text='Submit', command=self.submit_name)
            button2.pack()
        else:
        button3 = tki.Button(top, text='Cancel', command=lambda: self.top.destroy())
        button3.pack()

    def submit_name(self):
        data = self.entry0.get()
        if data:
            global value
            value = data
            self.top.destroy()

gui = GUI()
gui.mainloop()