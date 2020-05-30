import tkinter as tk
import numpy as np

counter=0

def enable():
	estado='!disabled'
	f2=tk.Frame(root,bg='#6195e8').place(relx=0.15,relwidth=0.85,relheight=1.0)
	e=tk.Entry(f2,bd=0,relief='sunken')
	e.place(relx=0.3,rely=0.05,relwidth=0.15,relheight=0.05)
	#Save old buttons creater
	save_old_b=open('button_creator.py').read()
	#print(save_old_b)
	exec(save_old_b)
	b2=tk.Button(f2,text='+',command=lambda:agrega(e.get(),f2) )
	b2.place(relx=0.15,rely=0.05, relwidth=0.15, relheight=0.05)
	return  e



def agrega(e,f2):
	#Guarda la ppsición relativa del ultimo boton
	j=open('j.py').read()
	contador=int(open('contador.py').read())
	#crea el boton original, en la posicion del ultimo salvado 
	action='cp'+str(contador)+'='+"tk.Button(f2,text=str(e),relief='sunken').place(relx=0.25,rely=float(j),relwidth=0.15,relheight=0.05)"
	exec(action)
	print('cp'+str(contador))
	print(cp0)
	#Crea el boton de eliminación que elmina  el boton asociado  
	old='cp'+str(contador)+'.destroy()'
	delet_Button_j=tk.Button(f2,text='X',relief='solid',command=exec(old) )
	delet_Button_j.place(relx=0.41,rely=float(j),relwidth=0.05,relheight=0.05)
	bsave=open('button_creator.py').read()
	bi=open('button_creator.py','w')
	#bi.write(bsave+"tk.Button(f2,text=str("+str(e)+"),relief='sunken').place(relx=0.25,rely=float("+j+"),relwidth=0.15,relheight=0.05)\n")
	stringer="tk.Button(f2,text='%(e)s',relief='sunken').place(relx=0.25,rely=%(j)s,relwidth=0.15,relheight=0.05)\n"% dict(e=e,j=j)
	stringer2="tk.Button(f2,text='X',relief='solid').place(relx=0.41,rely=%(j)s,relwidth=0.05,relheight=0.05)\n"% dict(j=j)
	contador=contador+1	
	bi.write(bsave+'cp'+str(contador)+'='+stringer+'delet_cp'+str(contador)+'='+stringer2)
	#Abre y escribe  el valor del contador 
	open('contador.py','w').write(str(contador))
	#cierra los documentos abiertos
	bi.close()
	#avanza en la posición relativa de "y" xrely
	c=float(j)+0.01+0.05
	myfile=open('j.py','w')
	myfile.write(str(c))
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

