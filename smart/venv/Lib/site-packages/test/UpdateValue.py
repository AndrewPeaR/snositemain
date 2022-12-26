import Tkinter as tk
import sys, random

class Shuffle(object):
    def __init__(self,master=None):
        self.master=master
        self.text=tk.Label(master, text="Type in something:")
        self.box=tk.Entry(master)
        self.buttn = tk.Button(master, text="Done", width=10, command=self.calc)
        self.globvar = tk.StringVar()
        self.globvar.set(0)
        self.result = tk.Label(self.master, textvariable=self.globvar)
    def hide(self):
        self.text.pack_forget()
        self.box.pack_forget()
        self.buttn.pack_forget()
        self.result.pack_forget()
    def show(self):
        self.text.pack(padx=2, pady=2)
        self.box.focus_set()
        self.box.pack(side=tk.TOP, padx=3, pady=3)
        self.buttn.pack(side=tk.TOP, padx=3, pady=3)
        self.result.pack(side=tk.TOP, padx=3, pady=3)
    def calc(self):
        word = self.box.get()
        while len(word) != 0:
            i = random.randrange(0, len(word))
            self.globvar.set(word[i])
            word = word[0:i] + word[i+1:]

class MainApp(object):
    def __init__(self,master=None):
        self.master=master
        app=self.app=tk.Tk()
        app.title("Mkee's Tools")
        app.geometry('500x500')
        menubar=tk.Menu(app)
        self.shuffle=Shuffle(master)
        self.current=self.shuffle
        program_menu=tk.Menu(menubar)
        program_menu.add_command(label='Shuffle',command=self.show_shuffle)
        menubar.add_cascade(label='Programs', menu=program_menu)
        app.config(menu=menubar)
    def show_shuffle(self):
        self.current.hide()
        self.current=self.shuffle
        self.shuffle.show()
    def show_buttons(self):
        self.current.hide()
        self.current=self.buttons        
        self.buttons.show()

def main():
    m=MainApp()
    m.app.mainloop()

if __name__=='__main__':
    main()