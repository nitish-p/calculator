# Python program to create a simple GUI
# calculator using Tkinter

from tkinter import *

from tkinter.simpledialog import askstring
history=[]
expression = ""
# Function to update expression in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    if num == ("\b"):
        expression = expression[:-1]
    else:
        expression = expression + str( num )

    equation.set( expression )
# Function to add history of the expression
def hist():
    global history
    global expression
    if history == []:
        equation.set( 0 ) # if empty set its value to 0
    else:
        expression = history[-1]
        equation.set( expression )
 #Function to evaluate the final expression
def equalpress():
    try:

        global expression
        total = str( eval( expression ) )

        equation.set( total )

        expression = str( total )

    except:

        equation.set( " error " )
        expression = ""
# Function to clear the contents of text entry box
def clear():
    global expression
    global history
    history = []
    history.append( expression )
    expression = ""
    equation.set( "" )
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    gui.configure( background="yellow" )
    gui.iconbitmap( r"C:/Users/patel/Downloads/123.ico" )
    gui.title( "Calculator" )

    gui.geometry( "520x420" )
    equation = StringVar()

    expression_field = Entry( gui, textvariable=equation, bg="pink", 
                        font=('calibri', 24, 'bold') )
    expression_field.grid( columnspan=4, ipadx=100 )

    equation.set( "enter ur expression" )

    button1 = Button( gui, text=' 1 ', fg='black', bg='grey',
                      command=lambda: press( 1 ), height=3, width=15 )
    button1.grid( row=2, column=0, pady=10 )

    button2 = Button( gui, text=' 2 ', fg='black', bg='grey',
                      command=lambda: press( 2 ), height=3, width=15 )
    button2.grid( row=2, column=1, pady=10 )

    button3 = Button( gui, text=' 3 ', fg='black', bg='grey',
                      command=lambda: press( 3 ), height=3, width=15 )
    button3.grid( row=2, column=2, pady=10 )

    button4 = Button( gui, text=' 4 ', fg='black', bg='grey',
                      command=lambda: press( 4 ), height=3, width=15 )
    button4.grid( row=3, column=0, pady=10 )

    button5 = Button( gui, text=' 5 ', fg='black', bg='grey',
                      command=lambda: press( 5 ), height=3, width=15 )
    button5.grid( row=3, column=1 )

    button6 = Button( gui, text=' 6 ', fg='black', bg='grey',
                      command=lambda: press( 6 ), height=3, width=15 )
    button6.grid( row=3, column=2 )

    button7 = Button( gui, text=' 7 ', fg='black', bg='grey',
                      command=lambda: press( 7 ), height=3, width=15 )
    button7.grid( row=4, column=0, pady=10 )

    button8 = Button( gui, text=' 8 ', fg='black', bg='grey',
                      command=lambda: press( 8 ), height=3, width=15 )
    button8.grid( row=4, column=1 )

    button9 = Button( gui, text=' 9 ', fg='black', bg='grey',
                      command=lambda: press( 9 ), height=3, width=15 )
    button9.grid( row=4, column=2 )

    button0 = Button( gui, text=' 0 ', fg='black', bg='grey',
                      command=lambda: press( 0 ), height=3, width=15 )
    button0.grid( row=5, column=0, pady=10 )

    plus = Button( gui, text=' + ', fg='black', bg='grey',
                   command=lambda: press( "+" ), height=3, width=15 )
    plus.grid( row=2, column=3 )

    minus = Button( gui, text=' - ', fg='black', bg='grey',
                    command=lambda: press( "-" ), height=3, width=15 )
    minus.grid( row=3, column=3 )

    multiply = Button( gui, text=' * ', fg='black', bg='grey',
                       command=lambda: press( "*" ), height=3, width=15 )
    multiply.grid( row=4, column=3 )

    divide = Button( gui, text=' / ', fg='black', bg='grey',
                     command=lambda: press( "/" ), height=3, width=15 )
    divide.grid( row=5, column=3 )

    equal = Button( gui, text=' = ', fg='black', bg='grey',
                    command=equalpress, height=3, width=15 )
    equal.grid( row=6, column=2 )

    clear = Button( gui, text='Clear', fg='black', bg='grey',
                    command=clear, height=3, width=15 )
    clear.grid( row=6, column='1' )

    decimal = Button( gui, text='.', fg='black', bg='grey',
                      command=lambda: press( "." ), height=3, width=15 )
    decimal.grid( row=5, column='1' )

    his = Button( gui, text='History', fg='black', bg='grey',
                  command=hist, height=3, width=15 )
    his.grid( row=6, column='0' )

    power = Button( gui, text='^', fg='black', bg='grey',
                    command=lambda: press( "**" ), height=3, width=15 )
    power.grid( row=5, column='2' )

    back = Button( gui, text='<-', fg='black', bg='grey',
                   command=lambda: press( "\b" ), height=3, width=15 )
    back.grid( row=6, column='3' )

    # start the GUI
    gui.mainloop()
