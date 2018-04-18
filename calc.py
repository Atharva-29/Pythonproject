import tkinter as tk
from functools import partial
import speech_recognition as sr
import playsound
from time import ctime
import time
import os
from gtts import gTTS
def speak(result1,result2,result3,result4,result5,result6):
    result1.config(text="Please speak operation!")
    time.sleep(2)
    print("Speak operation!")
    r = sr.Recognizer()
    r.energy_threshold = 15000
    with sr.Microphone() as source:
        audio = r.listen(source)
    opt=""
    try:
        opt = r.recognize_google(audio)
        result2.config(text=opt)
        print("You said :",opt)
    except sr.UnknownValueError:
        print("Could not understand audio")       
    except sr.RequestError as e:
        print("could not request results;{0}".format(e))
    data1 = recordAudio(result3,result4)
    result4.config(text=data1)
    data2 = recordAudio(result3,result4)
    result5.config(text=data2)
    if(opt == "addition"):
        s = int(data1) + int(data2) 
        result6.config(text=s)
        print("Sum of numbers is : ",s)
    elif(opt == "subtraction"):
        d = int(data1) - int(data2)
        result6.config(text=d)
        print("Difference of numbers is : ",d)
    elif(opt == "multiplication"):
        m = int(data1) * int(data2)
        result6.config(text=m)
        print("Product of numbers is : ",m)
    else:
        divide = float(data1) / float(data2)
        result6.config(text=divide)
        print("Division of numbers is : ",divide)
        
def recordAudio(result3,result4):
	r = sr.Recognizer()
	r.energy_threshold = 15000
	with sr.Microphone() as source:
		print("Speak Number!")
		result3.config(text="Speak number!")
		audio = r.listen(source)
	data = ""
	try:
		data = r.recognize_google(audio)
		print("You said: " + data)
		#result4.config(text=data)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return data
    
def add(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)+float(b)
	result3.config(text="Sum of numbers is %0.2f" % c)
def sub(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)-float(b)
	result3.config(text="Subtraction of numbers is %0.2f" % c)
def mul(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)*float(b)
	result3.config(text="Product of numbers is %0.2f" % c)
def div(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)/float(b)
	result3.config(text="Division of numbers is %0.2f" % c)
def clear():
    num1.delete(0,30)
    num2.delete(0,30)
    result1.config(text=" ")
    result2.config(text=" ")
    result3.config(text=" ")
    result4.config(text=" ")
    result5.config(text=" ")
root=tk.Tk()
root.geometry('500x350')
root.title("Calculator")
label=tk.Label(root,text="Number 1 :",fg="blue")
label.grid(row=2,column=0,padx=20,pady=10)
label1=tk.Label(root,text="Number 2 :",fg="blue")
label1.grid(row=3,column=0,padx=20,pady=10)
number1=tk.StringVar()
number2=tk.StringVar()
num1=tk.Entry(root,textvariable=number1)
num1.grid(row=2,column=1,pady=10)
num2=tk.Entry(root,textvariable=number2)
num2.grid(row=3,column=1,pady=10)
result1=tk.Label(root,fg="blue")
result1.grid(row=9,column=1)
result2=tk.Label(root,fg="blue")
result2.grid(row=10,column=1)
result3=tk.Label(root,fg="blue")
result3.grid(row=11,column=1)
result4=tk.Label(root,fg="blue")
result4.grid(row=12,column=1)
result5=tk.Label(root,fg="blue")
result5.grid(row=13,column=1)
result6=tk.Label(root,fg='blue')
result6.grid(row=14,column=1)
add=partial(add,result3,number1,number2)
addition=tk.Button(root,highlightbackground='purple',text="Add",width=6,command=add)
addition.grid(row=5,column=0,sticky='nse')
sub=partial(sub,result3,number1,number2)
subtraction=tk.Button(root,text="Subtract",width=6,highlightbackground='purple',command=sub)
subtraction.grid(row=5,column=1,sticky='nsw')
mul=partial(mul,result3,number1,number2)
multiplication=tk.Button(root,text="Multiply",width=6,highlightbackground='purple',command=mul)
multiplication.grid(row=6,column=0,sticky='nse')
div=partial(div,result3,number1,number2)
division=tk.Button(root,text="Divide",width=6,highlightbackground='purple',command=div)
division.grid(row=6,column=1,sticky='nsw')
clr=tk.Button(root,text="Clear",width=6,highlightbackground='purple',command=clear)
clr.grid(row=7,column=1,sticky='nsw')
speak=partial(speak,result1,result2,result3,result4,result5,result6)
say=tk.Button(root,text="Speak",highlightbackground='red',width=6,command=speak)
say.grid(row=7,column=0,sticky='nse')
root.mainloop()
    
             
        
             
            
            
