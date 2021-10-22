#!/usr/bin/env python
# coding: utf-8

# In[63]:


from tkinter import *
r=Tk()
i=Entry(r,width=50)
i.grid(column=0,row=0,padx=50,pady=40,columnspan=3)

def click(num):
    cu=i.get()
    i.delete(0,END)
    i.insert(0,str(cu) + str(num))
    return

def plus():
    cu=i.get()
    global fnum
    fnum= int(cu)
    i.delete(0,END)                        
    return

def minus():
    cu=i.get()
    global mnum
    mnum=int(cu)
    i.delete(0,END)
    return

def mul():
    cu=i.get()
    global multi
    multi=int(cu)
    i.delete(0,END)
    return

def divi():
    cu=i.get()
    global div_1
    div_1=int(cu)
    i.delete(0,END)
    return

def modulo():
    cu=i.get()
    global mod
    mod=int(cu)
    i.delete(0,END)
    return
    

def clear():
    i.delete(0,END)
    return

def ans():
    cu = i.get()
    snum = int(cu)
    i.delete(0, END)
    i.insert(0, str(fnum + snum))
    return
    mnumb= int(cu)
    i.delete(0,END)
    i.insert(0,str(mnum - mnumb))
    return    
    smul=int(cu)
    i.delete(0,END)
    i.insert(0,str(multi*smul))
    return
    
    div_2=int(cu)
    i.delete(0,END)
    i.insert(0,str(div_1//div_2))
    return
    
    mod_2=int(cu)
    i.delete(0,END)
    i.insert(0,str(mod%mod_2))
    return

b1=Button(r,text="1",command=lambda:click(1),padx=50,pady=25)
b1.grid(row=3,column=0)

b2=Button(r,text="2",command=lambda:click(2),padx=50,pady=25)
b2.grid(row=3,column=1)

b3=Button(r,text="3",command=lambda:click(3),padx=50,pady=25)
b3.grid(row=3,column=2)

b4=Button(r,text="4",command=lambda:click(4),padx=50,pady=25)
b4.grid(row=2,column=0)

b5=Button(r,text="5",command=lambda:click(5),padx=50,pady=25)
b5.grid(row=2,column=1)

b6=Button(r,text="6",command=lambda:click(6),padx=50,pady=25)
b6.grid(row=2,column=2)

b7=Button(r,text="7",command=lambda:click(7),padx=50,pady=25)
b7.grid(row=1,column=0)

b8=Button(r,text="8",command=lambda:click(8),padx=50,pady=25)
b8.grid(row=1,column=1)

b9=Button(r,text="9",command=lambda:click(9),padx=50,pady=25)
b9.grid(row=1,column=2)

b0=Button(r,text="0",command=lambda:click(0),padx=50,pady=25)
b0.grid(row=4,column=0)

b_plus=Button(r,text="+",command=plus,padx=50,pady=25)
b_plus.grid(row=4,column=1)

b_minus=Button(r,text="-",command=minus,padx=50,pady=25)
b_minus.grid(row=4,column=2)

b_clear=Button(r,text="Ac",command=clear,padx=46,pady=25)
b_clear.grid(row=5,column=0)

b_ans=Button(r,text="=",command=ans,padx=50,pady=25)
b_ans.grid(row=5,column=1)

b_mul=Button(r,text="*",command=mul,padx=50,pady=25)
b_mul.grid(row=5,column=2)

b_divi=Button(r,text="/",command=divi,padx=50,pady=25)
b_divi.grid(row=6,column=0)

b_modulo=Button(r,text="%",command=modulo,padx=49,pady=25)
b_modulo.grid(row=6,column=0)
 


r.mainloop()


# In[ ]:





# In[ ]:




