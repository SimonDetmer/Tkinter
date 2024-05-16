from tkinter import *

root = Tk()

header = Frame(root)
header.pack()
mainFrame = Frame(root)
mainFrame.pack()
footer = Frame(root)
footer.pack(fill=X)

text = '''
Ich
bin
ein
mehrzeiliger
Text
'''

def client_exit():
    print('Exit-Button wurde gedrückt')
    root.destroy()




w3 = Label(root, text='foo', fg='blue', bg='yellow', justify=LEFT)
w3.pack()

w2 = Label(header, text='Hi', fg='white', bg='red', font='courier')
w2.pack(side=LEFT)

w = Label(mainFrame, text=text, fg='blue', bg='yellow', justify=LEFT)
w.pack()

b = Button(footer, text='Exit', command=client_exit)
b.pack(fill=X)

if __name__ == '__main__':
    root.mainloop()

