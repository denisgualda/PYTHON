from tkinter import *
 
window = Tk()
 
window.title("CALCULA PORT SWITCH")
window.geometry('200x200')

#LABEL TITOL
lbl = Label(window, text="CALCULA PORTS SWITCH")
lbl.grid(row=0, sticky=W)


#ENTRA DADES
txt_nreflexe = Entry(window,width=10)
txt_nreflexe.grid(row=1, sticky=W)


#*^**********************************************************
##ACCIO DEL BOTO
def clicked():

        nreflexe = txt_nreflexe.get()
        nreflexe= int(nreflexe)

        #CALCULS *******
        if nreflexe >=1 and nreflexe <=48:
                nswitch = 1
                port = nreflexe
        elif nreflexe >=49 and nreflexe <=96:
                nswitch = 2
                port= nreflexe -48
        elif nreflexe >=97 and nreflexe <=144:
                nswitch = 3
                port= nreflexe - 96
        elif nreflexe >=145 and nreflexe <=192:
                nswitch = 4
                port = nreflexe - 144
        elif nreflexe >=193 and nreflexe <=240:
                nswitch = 5
                port = nreflexe - 192
        elif nreflexe >= 241 and nreflexe <=288:
                nswitch = 6
                port = nreflexe - 240
        elif nreflexe >=289 and nreflexe <=336:
                nswitch = 7
                port = nreflexe -288
        elif nreflexe >=337 and nreflexe <=384:
                nswitch = 8
                port =nreflexe - 336
        elif nreflexe >=385 and nreflexe <=432:
                nswitch = 9
                port = nreflexe - 384
        elif nreflexe >= 433 and nreflexe <=480:
                nswitch = 10
                port = nreflexe - 432
        elif nreflexe >= 481 and nreflexe <=528:
                nswitch = 11
                port = nreflexe - 480
        elif nreflexe >= 529 and nreflexe <=576:
                nswitch = 12
                port = nreflexe - 528
        elif nreflexe >= 577 and nreflexe <=624:
                nswitch = 13
                port = nreflexe - 576
        elif nreflexe >=625 and nreflexe <=672:
                nswitch = 14
                port = nreflexe - 624




#*^**********************************************************
#MOSTRA RESULTATS

        lresultat_switch.configure(text="SWITCH:  " + str(nswitch))
        lresultat_port.config(text="PORT:  " + str(port))


#*^**********************************************************
##GUI - BOTO
btn = Button(window, text="Calcula Port", command=clicked)
btn.grid(row=3, sticky=W)
#*^**********************************************************

#*^**********************************************************
#GUI - LABEL RESULTAT

#switch
lresultat_switch = Label(window ,text="-")
lresultat_switch.grid(row=4, sticky=W)

#port
lresultat_port = Label(window ,text="-")
lresultat_port.grid(row=6, sticky=W)

#*^**********************************************************

window.mainloop()