
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import gammu
import sys

# this is a function to get the user input from the text input box
def getPhoneNumber():
	userInput = phone_number.get()
	return userInput


# this is a function to get the user input from the text input box
def getTextMessage():
	userInput = text_message.get()
	return userInput

# this is the function called when the button is clicked
def makeCall():
	state_machine.DialVoice(getPhoneNumber())


# this is the function called when the button is clicked
def endCall():
	state_machine.CancelCall(1, True)

# this is the function called when the button is clicked
def sendSMS():
	message = {
    'Text': getTextMessage(),
    'SMSC': {'Location': 1},
    'Number': getPhoneNumber(),
	}

	state_machine.SendSMS(message)
	messagebox.showinfo(title='Message Sent', message="SENT!")



root = Tk()
state_machine = gammu.StateMachine()
state_machine.ReadConfig()
state_machine.Init()

# This is the section of code which creates the main window
root.geometry('800x520')
root.configure(background='#F0F8FF')
root.title('Messenger')


# This is the section of code which creates the a label
Label(root, text='Phone', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=123, y=107)


# This is the section of code which creates the a label
Label(root, text='Text', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=123, y=147)


# This is the section of code which creates a text input box
phone_number=Entry(root)
phone_number.place(x=203, y=107)


# This is the section of code which creates a text input box
text_message=Entry(root)
text_message.place(x=203, y=147)


# This is the section of code which creates a button
Button(root, text='Send Text', bg='#F0F8FF', font=('arial', 12, 'normal'), command=sendSMS).place(x=213, y=207)

# This is the section of code which creates a button
Button(root, text='Make Call', bg='#F0F8FF', font=('arial', 12, 'normal'), command=makeCall).place(x=213, y=267)


# This is the section of code which creates a button
Button(root, text='End Call', bg='#FF0000', font=('arial', 12, 'normal'), command=endCall).place(x=213, y=337)

root.mainloop()

