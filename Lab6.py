Câu 1
from tkinter import *

def close_window():
    root.destroy()  # destroying the main window

root = Tk()
frame = Frame(root)
frame.pack()

button = Button(frame)
button['text'] ="Good-bye."
button['command'] = close_window
button.pack()

mainloop()

#Câu 2
from tkinter import *

root = Tk()
root.geometry("200x200")
root.title("My Button Increaser")

global counter
counter = 0

def nClick():
    global counter
    counter += 1
    mButton1.config(text = counter)

mButton1 = Button(text = counter, command = nClick, fg = "darkgreen", bg = "white")
mButton1.pack()

root.mainloop()

#Câu 3
def x(): 
    return y
#Câu 4:
import tkinter

def count(text, out_data):
    data = text.get('0.0', tkinter.END)
    counts = {}
    for char in 'ATCG':
        counts[char] = data.count(char)
    print(counts)
    out_data.set('Num As: {0} Num Ts: {1} Num Cs: {2} Num Gs: {3}'.format(
     counts['A'], counts['T'], counts['C'], counts['G']))

window = tkinter.Tk()
text = tkinter.Text(window, height=10, width=40)
text.pack()

out_data = tkinter.StringVar()

button = tkinter.Button(window, text='Count', command=lambda: count(text,
out_data))
button.pack()

label = tkinter.Label(window, textvar=out_data)
label.pack()

window.mainloop()

#Câu 5:
import tkinter

def convert(f_temp, c_temp):
    f = f_temp.get()
    c_temp.set('{:.1f}'.format((f - 32) * 5 / 9))

window = tkinter.Tk()
frame = tkinter.Frame(window).pack()

f_temp = tkinter.DoubleVar()
c_temp = tkinter.StringVar()

tkinter.Label(frame, text='Temperature in Fahrenheit:').pack()

text = tkinter.Entry(frame, textvar=f_temp).pack()

label = tkinter.Label(window, textvar=c_temp).pack()

button = tkinter.Button(window, text='Convert', command=lambda: convert(f_temp,
c_temp))
button.pack()

button = tkinter.Button(window, text='Quit', command=lambda: window.destroy())
button.pack()

window.mainloop()

#Câu 6:
import tkinter
import tkinter.filedialog as dialog

class TextEditor:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()

        self.text = tkinter.Text(parent)
        self.text.pack()

        menubar = tkinter.Menu(parent)
        filemenu = tkinter.Menu(menubar)
        filemenu.add_command(label='Save', command=self.save_click)
        filemenu.add_command(label='Quit', command=self.quit_click)
        menubar.add_cascade(label='File', menu=filemenu)
        window.config(menu=menubar)
    
    def save_click(self):
        data = self.text.get('0.0', tkinter.END)
        filename = dialog.asksaveasfilename(
         parent=self.parent,
         filetypes=[('Text', '*.txt')],
         title='Save as...')
        writer = open(filename, 'w')
        writer.write(data)
        writer.close()
    
    def quit_click(self):
        self.parent.destroy()

if __name__ == '__main__':
    window = tkinter.Tk()
    app = TextEditor(window)
    window.mainloop()
