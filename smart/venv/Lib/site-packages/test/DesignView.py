'''
Created on Apr 26, 2013

@author: user
'''
from Tkinter import Text, Scrollbar, Tk, Button, Label
import Tkinter
import webbrowser
from py_w3c.validators.html.validator import HTMLValidator

root = Tk()
root.title("Editor's View")
text = Text(root, wrap="word", background="white", borderwidth=0, highlightthickness=0)
vsb = Scrollbar(root, orient="vertical", borderwidth=1,command=text.yview)
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y", expand=False)
text.pack(side="left", fill="both", expand=True)
text.tag_configure("error", foreground="red", underline=True)

def BrowserOpen():
    url='/home/user/workspace/Problem Statement Two/StatementTwo/files/25 errors - a1 (1).html'
    controller = webbrowser.get('Firefox')
    controller.open(url)

def SaveContent():
    txt = open('/home/user/workspace/Problem Statement Two/StatementTwo/files/25 errors - a1 (1).html', 'w')
    txt.write(text.get(0.0, Tkinter.END))
    txt.close()

def key(event):
    if event.char == '\x1b':
        root.destroy()
    else:
        val = text.index(Tkinter.INSERT).split('.')
        lineNum.config(text=str(val[0]))
        colNum.config(text=str(val[1]))

vld = HTMLValidator(doctype = "HTML 4.01 Strict")
vld.validate_file('/home/user/workspace/Problem Statement Two/StatementTwo/files/25 errors - a1 (1).html')
errors = vld.errors
locationList=[]

for error in range(len(errors)):
    locationList.append(errors[error]['line'])
print locationList
txt = open('/home/user/workspace/Problem Statement Two/StatementTwo/files/25 errors - a1 (1).html', 'r')
lineNum=1
errorIndex=0
for line in txt:
    '''
    #print line
    print lineNum, ' line num'
    print locationList[errorIndex][0], ' error index'
    print errorIndex , ' index'
    if str(lineNum) == str(locationList[errorIndex][0]):
        print 'this is line :: ', lineNum, ' with error :: ', locationList[errorIndex][0]
        errorIndex+=1
    lineNum+=1
    '''
    
    line.strip()
    print line.strip()
    #text.tag_add('error', 1.5, 1.9)
    text.insert(Tkinter.END,line)
    
txt.close()


browse = Button(root, text='Open Browser', command=BrowserOpen)
browse.pack(fill='x', side='top')

save = Button(root, text='Save', command=SaveContent)
save.pack(fill='x', side='top')

lineNum = Label(root, text='')
lineNum.pack(fill='x', side='bottom')

line = Label(root, text='Line')
line.pack(fill='x', side='bottom')

colNum = Label(root, text='')
colNum.pack(fill='x', side='bottom')

col = Label(root, text='Column')
col.pack(fill='x', side='bottom')

quit = Button(root, text='Quit', command=root.destroy)
quit.pack(fill='x', side='top')

root.bind_all('<Key>', key)
root.mainloop() 