from Tkinter import Tk, Label
root = Tk()
prompt = ' Press any key '
label1 = Label(root, text=prompt, width=len(prompt), bg='yellow')
label1.pack()
def key(event):
    if event.char != event.keysym:
        msg = 'Special Key %r' % event.keysym
        label1.config(text=msg)
    else:
        print "WALA!"
root.bind_all('<Key>', key)
root.mainloop()