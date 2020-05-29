import tkinter as tk
import numpy as np

e1=0
estado='disabled'

def enable():
	estado='!disabled'
	f2=tk.Frame(root,bg='#6195e8').place(relx=0.15,relwidth=0.85,relheight=1.0)
	e=tk.Entry(f2,bd=0,relief='sunken')
	e.place(relx=0.3,rely=0.05,relwidth=0.15,relheight=0.05)
	b2=tk.Button(f2,text='+',command=lambda:agrega(e.get(),f2) )
	b2.place(relx=0.15,rely=0.05, relwidth=0.15, relheight=0.05)
	return  e

def agrega(e,f2):
	tk.Button(f2,text=str(e),relief='sunken').place(relx=0.25,rely=0.12,relwidth=0.15,relheight=0.05)
	return

root=tk.Tk()

root['width']=1000
root['height']=700

#Create first frame
f1=tk.Frame(root,bg='#88abe3',width=1000,height=1000).place(relwidth=1.0,relheight=1.0)
#Principal  button productive center!
b1=tk.Button(f1,text='Centros Prodictivos',relief='sunken',command=enable)
b1.place(relx=0.0,rely=0.1,relwidth=0.15,relheight=0.05)


root.mainloop()
