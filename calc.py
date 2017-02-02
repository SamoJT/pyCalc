import sys
from tkinter import *


class Gui:


    def __init__(self, root):
        btn = 0
        self.tst = []
        self.root = root

        self.label = Label(self.root,text=btn,background='GREEN')
        self.label.pack(fill=BOTH,expand=True)

        self.frame = Frame(self.root,borderwidth=0)
        self.frame.pack(fill=BOTH,expand=True)
        self.button1 = Button(self.frame, text='1', command=lambda: self.press('1'))
        self.button2 = Button(self.frame, text='2', command=lambda: self.press('2'))
        self.button3 = Button(self.frame, text='3', command=lambda: self.press('3'))
        self.buttonCE = Button(self.frame, text='CE', command=lambda: self.clear())
        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack(side=LEFT)
        self.buttonCE.pack(side=LEFT)

        self.frame = Frame(self.root,borderwidth=0)
        self.frame.pack(fill=BOTH,expand=True)
        self.button4 = Button(self.frame, text='4', command=lambda: self.press('4'))
        self.button5 = Button(self.frame, text='5', command=lambda: self.press('5'))
        self.button6 = Button(self.frame, text='6', command=lambda: self.press('6'))
        self.buttonX = Button(self.frame, text='X', command=lambda: self.num1(y = False, mul = True, div = False))
        self.button4.pack(side=LEFT)
        self.button5.pack(side=LEFT)
        self.button6.pack(side=LEFT)
        self.buttonX.pack(side=LEFT)

        self.frame = Frame(self.root,borderwidth=0)
        self.frame.pack(fill=BOTH,expand=True)
        self.button7 = Button(self.frame, text='7', command=lambda: self.press('7'))
        self.button8 = Button(self.frame, text='8', command=lambda: self.press('8'))
        self.button9 = Button(self.frame, text='9', command=lambda: self.press('9'))
        self.buttonDiv = Button(self.frame, text='/', command=lambda: self.num1(y = False, mul = False, div = True))
        self.button7.pack(side=LEFT)
        self.button8.pack(side=LEFT)
        self.button9.pack(side=LEFT)
        self.buttonDiv.pack(side=LEFT)

        self.frame = Frame(self.root,borderwidth=0)
        self.frame.pack(fill=BOTH,expand=True)
        self.buttonAdd = Button(self.frame, text='+', command=lambda: self.num1(y = False, mul = False, div = False))
        self.button0 = Button(self.frame, text='0', command=lambda: self.press('0'))
        self.buttonMin = Button(self.frame, text='-', command=lambda: self.press('-'))
        self.buttonEq = Button(self.frame, text='=', command=lambda: self.num1(y = True, mul = False, div = False))

        self.buttonAdd.pack(side=LEFT)
        self.button0.pack(side=LEFT)
        self.buttonMin.pack(side=LEFT)
        self.buttonEq.pack(side=LEFT)

        self.running_tot = []


    def press(self, x):
        self.tst += x
        self.tst = "".join(self.tst)
        self.label.config(text=self.tst)
        print(self.tst)


    def num1(self, y, mul, div):

        running_tot = self.running_tot

        if y == False:
        	if mul == True:
        		running_tot.append(self.tst)
        		running_tot.append('x')
        		print(running_tot) #DEBUG
        		self.tst = []
        		self.label.config(text=self.tst)
        	elif div == True:
        		running_tot.append(self.tst)
        		running_tot.append('/')
        		print(running_tot) #DEBUG
        		self.tst = []
        		self.label.config(text=self.tst)
        	else:
        		running_tot.append(self.tst)
        		print(running_tot) #DEBUG
        		self.tst = []
        		self.label.config(text=self.tst)

        elif y == True:
            running_tot.append(self.tst)
            print(running_tot) #DEBUG
            self.tst = []
            self.label.config(text=self.tst)

            ans = 0
            skip = False
            times = False
            div = False

            for i in running_tot:
            	if i == 'x':
            		skip = True
            		times = True
            		continue
            	if i == '/':
            		skip = True
            		div = True
            		continue
            	elif times == True:
            		i = int(i)
            		ans = ans*i
            		skip = False
            		times = False
            	elif div == True:
            		i = int(i)
            		ans = ans/i
            		skip = False
            		div = False
            	else:
            		i = int(i)
            		ans += i

            print(ans) #DEBUG
            self.label.config(text=ans)

        return(self.num1, running_tot)

    def clear(self):
        self.label.config(text=0)
        self.running_tot = []



def main():
    root = Tk()
    gui = Gui(root)
    #root.geometry('%dx%d' % (500,460))
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())