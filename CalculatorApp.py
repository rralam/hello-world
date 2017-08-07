#I have imported all the members from the module
from tkinter import *

calculator = Tk()
calculator.title("CALCULATOR")
calculator.resizable(0,0) #0 for not resizeable and 1 for resizeable

#Class for this Application with parameter Frame
class Application(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame. __init__(self,master,*args,**kwargs)
        self.createWidget()

    def replaceText(self,text):
        self.display.delete(0,END)
        self.display.insert(0,text)

    #we need a function that makes sure that the the 0 is gone when the user inputs the numbers for the first time.
    def appendText(self,text):
        
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength,text)

     #function for Clear Button
    def clearText(self):
        self.replaceText("0")

    #I am going to calculate the result when the user clicks the equal button
    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%","/100")
        
        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("Error","invalid Input")

#creating the widgets i.e. the buttons and the display
    def createWidget(self):
        self.display = Entry(self,font = ("Helvetica",16),borderwidth=0,relief=RAISED, justify = RIGHT)
        self.display.insert(0,"0")
        self.display.grid(row= 0, column= 0, columnspan = 5)
    

#the following are the code for buttons 7,8,9,*,C :

        #Button for number seven
        self.sevenButton = Button(self, font=("Helvetica",10),text = "7", borderwidth = 0, command= lambda:self.appendText("7"))
        self.sevenButton.grid(row=1,column=0, sticky ="NWNESWSE" )

        #Button for number eight
        self.eightButton = Button(self, font=("Helvetica",11),text = "8",borderwidth = 0, command= lambda:self.appendText("8"))
        self.eightButton.grid(row=1,column=1, sticky ="NWNESWSE" )

        #Button for number nine
        self.nineButton = Button(self, font=("Helvetica",11),text = "9",borderwidth = 0, command= lambda:self.appendText("9"))
        self.nineButton.grid(row=1,column=2, sticky ="NWNESWSE" ) 

        #Button for Multiplcation sign
        self.timesButton = Button(self, font=("Helvetica",11),text = "*",borderwidth = 0, command= lambda:self.appendText("*"))
        self.timesButton.grid(row=1,column=3, sticky ="NWNESWSE" )
        
        #Button for Clear
        self.clearButton = Button(self, font=("Helvetica",11),text = "C",borderwidth = 0, command = lambda:self.clearText())
        self.clearButton.grid(row=1,column=4, sticky ="NWNESWSE" )

#the following are the code for buttons 4,5,6,/,% :

        self.fourButton = Button(self, font=("Helvetica",10),text = "4",borderwidth = 0, command= lambda:self.appendText("4"))
        self.fourButton.grid(row=2,column=0, sticky ="NWNESWSE" )
       
        self.fiveButton = Button(self, font=("Helvetica",11),text = "5",borderwidth = 0, command= lambda:self.appendText("5"))
        self.fiveButton.grid(row=2,column=1, sticky ="NWNESWSE" )
        
        self.sixButton = Button(self, font=("Helvetica",11),text = "6",borderwidth = 0, command= lambda:self.appendText("6"))
        self.sixButton.grid(row=2,column=2, sticky ="NWNESWSE" ) 
        
        self.divideButton = Button(self, font=("Helvetica",11),text = "/",borderwidth = 0, command= lambda:self.appendText("/"))
        self.divideButton.grid(row=2,column=3, sticky ="NWNESWSE" )
               
        self.percentButton = Button(self, font=("Helvetica",11),text = "%",borderwidth = 0, command= lambda:self.appendText("%"))
        self.percentButton.grid(row=2,column=4, sticky ="NWNESWSE")

#For buttons 1,2,3,-,=:

        self.oneButton = Button(self, font=("Helvetica",10),text = "1",borderwidth = 0, command= lambda:self.appendText("1"))
        self.oneButton.grid(row=3,column=0, sticky ="NWNESWSE" )
       
        self.twoButton = Button(self, font=("Helvetica",11),text = "2",borderwidth = 0, command= lambda:self.appendText("2"))
        self.twoButton.grid(row=3,column=1, sticky ="NWNESWSE" )
        
        self.threeButton = Button(self, font=("Helvetica",11),text = "3",borderwidth = 0, command= lambda:self.appendText("3"))
        self.threeButton.grid(row=3,column=2, sticky ="NWNESWSE" ) 
        
        self.minusButton = Button(self, font=("Helvetica",11),text = "-",borderwidth = 0, command= lambda:self.appendText("-"))
        self.minusButton.grid(row=3,column=3, sticky ="NWNESWSE" )

        self.equalButton = Button(self, font=("Helvetica",11),text = "=",borderwidth = 0, command= lambda:self.calculateExpression())
        self.equalButton.grid(row=3,column=4, sticky ="NWNESWSE",rowspan=2 )

#For button 0,.,+ :

        self.zeroButton = Button(self, font=("Helvetica",10),text = "0",borderwidth = 0, command= lambda:self.appendText("0"))
        self.zeroButton.grid(row=4,column=0, sticky ="NWNESWSE",columnspan=2 )
       
        self.dotButton = Button(self, font=("Helvetica",11),text = ".",borderwidth = 0, command= lambda:self.appendText("."))
        self.dotButton.grid(row=4,column=2, sticky ="NWNESWSE" )
        
        self.plusButton = Button(self, font=("Helvetica",11),text = "+",borderwidth = 0, command= lambda:self.appendText("+"))
        self.plusButton.grid(row=4,column=3, sticky ="NWNESWSE") 
        


app = Application(calculator).grid()

#This displays the window
calculator.mainloop()
