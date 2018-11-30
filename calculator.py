#Python program to create  a simple GUI
#calculator using Tkinter

#import everything from tkinter module, In python3.x is tkinter and in python 2.x is Tkinter
from tkinter import *
import math
calculator= Tk() #Create a main window
calculator.title("Calculator")
calculator.resizable(0,0) #Prevents the calculator from being resized both horizontslly and vertically.


class Application(Frame): 
    def __init__(self, master, width=0, height=0 , *args, **kwargs): #Methods,received the instance self automatically, Constructor, master = calculator
        Frame.__init__(self, master, *args, **kwargs) #Create a frame (containter that hold thw widgets) in the window (master)
        self.createWidgets()
    

    def square(self):
        self.new=self.display.get()
        try:
            self.value=eval(self.new)
        except SyntaxError or NameError:
            self.display.delete(0,END)
            self.display.insert(0,'Invalid Input!')
        else:
            self.sqval=pow(self.value,2)
            self.display.delete(0,END)
            self.display.insert(0,self.sqval)
           
       
 
    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def clearText(self):
        self.replaceText("0")

    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/ 100")
        self.expression = self.expression.replace("x", "*")
 
        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("Error", "Invalid Input")
        
 
 

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)
 
        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)
            

    def createWidgets(self):
        self.display = Entry(self, font=("Arial", 18), width=50 , bd=0 , bg="gray80", relief=RAISED, justify=RIGHT) #Create a input field inside the frame
        self.display.insert(0,"0") #default text is 0
        self.display.grid(row=0, column=0, columnspan=4)

        #First Row
        
        self.clearButton = Button(self, font=("Arial", 18), text="AC", activebackground="PaleVioletRed1", activeforeground="MediumPurple1", width=10, bd=0 , command=lambda: self.clearText()) #command:call function
        self.clearButton.grid(row=1, column=0, sticky="NWNESWSE")#sticky: button occupy the full width of the column

        self.squareButton = Button(self, font=("Arial", 18), text="x²", activebackground="PaleVioletRed1", activeforeground="MediumPurple1", width=10 , bd=0 , command=lambda: self.square())
        self.squareButton.grid(row=1, column=1, sticky="NWNESWSE")

        self.percentageButton = Button(self, font=("Arial", 18), text="%", activebackground="PaleVioletRed1", activeforeground="MediumPurple1", width=10 , bd=0 , command=lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=1, column=2, sticky="NWNESWSE")

        self.divisionButton = Button(self, font=("Arial", 18), text="/", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0 , command=lambda: self.appendToDisplay("/"))
        self.divisionButton.grid(row=1, column=3, sticky="NWNESWSE")

        #Second Row

        self.sevenButton = Button(self, font=("Arial", 18), text="7", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=2, column=0, sticky="NWNESWSE")

        self.eightButton = Button(self, font=("Arial", 18), text="8", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=2, column=1, sticky="NWNESWSE")

        self.nineButton = Button(self, font=("Arial", 18), text="9", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=2, column=2, sticky="NWNESWSE")

        self.timesButton = Button(self, font=("Arial", 18), text="x", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("x"))
        self.timesButton.grid(row=2, column=3, sticky="NWNESWSE")

        #Third Row

        self.fourButton = Button(self, font=("Arial", 18), text="4", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=3, column=0, sticky="NWNESWSE")

        self.fiveButton = Button(self, font=("Arial", 18), text="5", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=3, column=1, sticky="NWNESWSE")

        self.sixButton = Button(self, font=("Arial", 18), text="6", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=3, column=2, sticky="NWNESWSE")

        self.minusButton = Button(self, font=("Arial", 18), text="-", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column=3, sticky="NWNESWSE")

        #Fourth Row

        self.oneButton = Button(self, font=("Arial", 18), text="1", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=4, column=0, sticky="NWNESWSE")

        self.twoButton = Button(self, font=("Arial", 18), text="2", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=4, column=1, sticky="NWNESWSE")

        self.threeButton = Button(self, font=("Arial", 18), text="3", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=4, column=2, sticky="NWNESWSE")

        self.plusButton = Button(self, font=("Arial", 18), text="+", bg="plum2", activebackground="PaleVioletRed1",  activeforeground="MediumPurple1", width=10 , bd=0, command=lambda: self.appendToDisplay("+"))
        self.plusButton.grid(row=4, column=3, sticky="NWNESWSE")

        #Five Row

        
        self.zeroButton = Button(self, font=("Arial", 18), text="0", bg="plum2", activebackground="PaleVioletRed1", width=10 , bd=0, command=lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=5, column=0, sticky="NWNESWSE", columnspan=2)

        self.dotButton = Button(self, font=("Arial", 18), text=".", bg="plum2", activebackground="PaleVioletRed1", width=10 , bd=0, command=lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=5, column=2, sticky="NWNESWSE")

        self.equalButton = Button(self, font=("Arial", 18), text="=", bg="plum2", activebackground="PaleVioletRed1", width=10 , bd=0, command=lambda: self.calculateExpression())
        self.equalButton.grid(row=5, column=3, sticky="NWNESWSE")



    

app = Application(calculator).grid() #grid(): organizes the widgets in grid before placnig in the parent widget.
calculator.mainloop() # Its infinite loop to run application
