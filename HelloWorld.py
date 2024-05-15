from tkinter import *

root = Tk()

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


w = Label(root, text=text, fg='blue', bg='yellow', justify=LEFT)
w.pack()

w2 = Label(root, text='Hi', fg='white', bg='red', font='courier')
w2.pack(side=LEFT)

b = Button(root, text='Exit', command=client_exit)
b.pack()

if __name__ == '__main__':
    root.mainloop()

