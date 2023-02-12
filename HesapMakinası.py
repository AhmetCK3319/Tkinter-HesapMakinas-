from tkinter import *
pencere=Tk()
pencere.title("Hesap Makinası")
pencere.geometry("270x250+300+100")
pencere.resizable(FALSE,FALSE)
depo=""

def hesapla(tus):
    global depo
    if tus in "0123456789":
        ekran.insert(END,tus)
        depo=depo+tus
    if tus in "+-/*":
        ekran.insert(END,tus)
        depo=depo+tus
    if tus == "=":
        ekran.delete(0,END)
        hesap=eval(depo,{"__builtins":None})
        depo=str(hesap)
        ekran.insert(END,depo)
    if tus == "C":
        ekran.delete(0,END)
        depo=""
                    
        

ekran=Entry(width=40,justify=RIGHT)
ekran.grid(row=0,column=0,columnspan=3,ipady=4)

liste=["1","2","3","4","5","6","7","8","9","0","+","-","/","*","=","C"]
stun=0
sıra=1
for i in liste:
    komut=lambda x=i : hesapla(x)
    Button(text=i,width=10,font="verdana 8 bold",height=2,relief=GROOVE,command=komut).grid(row=sıra,column=stun)
    stun +=1
    if stun >2:
        stun=0
        sıra+=1
mainloop()   