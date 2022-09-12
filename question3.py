#question 3
#making a GUI calendar using python


#importing all modules of tkinter
from tkinter import*
 
def find_month_calendar(): #function to obtain month and year, it is a command
    month=int(monthspinbox.get()) #defined by the user and it must be an integer
    year=int(yearspinbox.get()) #defined by the user
    details=calendar.month(year,month)
    textfield.delete(0.0,END) #DELETES OLD DATA
    textfield.insert(INSERT,details)

import calendar  #importing the calendar module
#creating a main window
main=Tk()  #Using the Tk
#formating the window
main.title("My first window") #changing my window title
main.maxsize(width=300,height=800) #maxmized size
main.minsize(width=100,height=200) #minimized size
main.config(bg="#7575dd")

# creating widgets; labels, button, checkbox,images
month=Label(main,text="Month",font=("georgina",15,"bold"),bg="#7575dd",fg="#ff1d58")
month.pack()
month.grid() #creates a table-like structure
# month=Entry(main,bd=5,width=100) for username

year=Label(main,text="Year",font=("georgina",15,"bold"),bg="#7575dd",fg="#ff1d58")
year.grid(row=0,column=1)

s=PhotoImage(file="D:/WomenInTechCohot2/PythonDevelopment/images/image.png")
ss=Label(main,image=s,width=30,height=30)
ss.place(x=100,y=5) #place it at x and y planes

#creating a spin box for month
monthspinbox=Spinbox(main,from_=1,to=12,width=8,font=("georgina",12,"bold"),bg="green")
monthspinbox.grid(row=1,column=0,padx=10)

#creating a spin box for year
yearspinbox=Spinbox(main,from_=1995,to=2030,width=8,font=("georgina",12,"bold"),bg="green")
yearspinbox.grid(row=1,column=1,padx=10) #padding between year and month columns

#creating button
goButton=Button(main,text="Find",font=("georgina",15,"bold"),command=find_month_calendar,bg="green")
goButton.grid(row=1,column=2,padx=10)

#creating a textfield
textfield=Text(main,width=24,height=8,fg="green")
textfield.grid(row=2,column=0,columnspan=3)

main.mainloop() #main window
#creating a gui calendar using the tkinter library in python

