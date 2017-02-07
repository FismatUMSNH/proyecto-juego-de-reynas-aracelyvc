from Tkinter import*
import tkMessageBox
import random




def tirop1():
    global op1
    global op2
    global carta1p1
    global carta2p1
    global carta3p1
    global carta4p1
    global carta5p1
    global carta1p2
    global carta2p2
    global carta3p2
    global carta4p2
    global carta5p2
    global cardsA
    c1=card1p1.get()
    c2=card2p1.get()
    c3=card3p1.get()
    c4=card4p1.get()
    c5=card5p1.get()
    cards = c1+c2+c3+c4+c5
    cardsB = cardsA
    cardsA += cards
    if cards==1:
        if c1==1:
            if carta1p1==41 or carta1p1==42 or carta1p1==43 or carta1p1==44 or carta1p1==45 or carta1p1==46 or carta1p1==47 or carta1p1==48:
                lblp1=Label(ventana,text="Escoge una reina").grid(row=0,column=5)
                op1 = 1
            elif carta1p1==64 or carta1p1==65 or carta1p1==66 or carta1p1==67:
                lblp1=Label(ventana,text="Duerme una reina").grid(row=0,column=5)
                op1=2
            elif carta1p1==49 or carta1p1==50 or carta1p1==51 or carta1p1==52:
                lblp1=Label(ventana,text="Roba una reina  ").grid(row=0,column=5)
                op1=3
            elif (carta1p1==58 or carta1p1==59 or carta1p1==60) and op2==2:
                op2=0
            elif (carta1p1==61 or carta1p1==62 or carta1p1==63) and op2==3:
                op2=0
            elif carta1p1==53 or carta1p1==54 or carta1p1==55 or carta1p1==56 or carta1p1==57:
                jk=1
            boton1 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='red',variable=card1p1,onvalue=1,offvalue=0).grid(row=0,column=0)
            carta1p1=vector2[cardsA]
        elif c2==1:
            if carta2p1==41 or carta2p1==42 or carta2p1==43 or carta2p1==44 or carta2p1==45 or carta2p1==46 or carta2p1==47 or carta2p1==48:
                lblp1=Label(ventana,text="Escoge una reina").grid(row=0,column=5)
                op1 = 1
            elif carta2p1==64 or carta2p1==65 or carta2p1==66 or carta2p1==67:
                lblp1=Label(ventana,text="Duerme una reina").grid(row=0,column=5)
                op1=2
            elif carta2p1==49 or carta2p1==50 or carta2p1==51 or carta2p1==52:
                lblp1=Label(ventana,text="Roba una reina  ").grid(row=0,column=5)
                op1=3
            elif (carta2p1==58 or carta2p1==59 or carta2p1==60) and op2==2:
                op2=0
            elif (carta2p1==61 or carta2p1==62 or carta2p1==63) and op2==3:
                op2=0
            elif carta2p1==53 or carta2p1==54 or carta2p1==55 or carta2p1==56 or carta2p1==57:
                jk=1
            boton2 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='red',variable=card2p1,onvalue=1,offvalue=0).grid(row=0,column=1)
            carta2p1=vector2[cardsA]
        elif c3==1:
            if carta3p1==41 or carta3p1==42 or carta3p1==43 or carta3p1==44 or carta3p1==45 or carta3p1==46 or carta3p1==47 or carta3p1==48:
                lblp1=Label(ventana,text="Escoge una reina").grid(row=0,column=5)
                op1 = 1
            elif carta3p1==64 or carta3p1==65 or carta3p1==66 or carta3p1==67:
                lblp1=Label(ventana,text="Duerme una reina").grid(row=0,column=5)
                op1=2
            elif carta3p1==49 or carta3p1==50 or carta3p1==51 or carta3p1==52:
                lblp1=Label(ventana,text="Roba una reina  ").grid(row=0,column=5)
                op1=3
            elif (carta3p1==58 or carta3p1==59 or carta3p1==60) and op2==2:
                op2=0
            elif (carta3p1==61 or carta3p1==62 or carta3p1==63) and op2==3:
                op2=0
            elif carta3p1==53 or carta3p1==54 or carta3p1==55 or carta3p1==56 or carta3p1==57:
                jk=1
            boton3 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='red',variable=card3p1,onvalue=1,offvalue=0).grid(row=0,column=2)
            carta3p1=vector2[cardsA]
        elif c4==1:
            if carta4p1==41 or carta4p1==42 or carta4p1==43 or carta4p1==44 or carta4p1==45 or carta4p1==46 or carta4p1==47 or carta4p1==48:
                lblp1=Label(ventana,text="Escoge una reina").grid(row=0,column=5)
                op1 = 1
            elif carta4p1==64 or carta4p1==65 or carta4p1==66 or carta4p1==67:
                lblp1=Label(ventana,text="Duerme una reina").grid(row=0,column=5)
                op1=2
            elif carta4p1==49 or carta4p1==50 or carta4p1==51 or carta4p1==52:
                lblp1=Label(ventana,text="Roba una reina  ").grid(row=0,column=5)
                op1=3
            elif (carta4p1==58 or carta4p1==59 or carta4p1==60) and op2==2:
                op2=0
            elif (carta4p1==61 or carta4p1==62 or carta4p1==63) and op2==3:
                op2=0
            elif carta4p1==53 or carta4p1==54 or carta4p1==55 or carta4p1==56 or carta4p1==57:
                jk=1
            boton4 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='red',variable=card4p1,onvalue=1,offvalue=0).grid(row=0,column=3)
            carta4p1=vector2[cardsA]
        elif c5==1:
            if carta5p1==41 or carta5p1==42 or carta5p1==43 or carta5p1==44 or carta5p1==45 or carta5p1==46 or carta5p1==47 or carta5p1==48:
                lblp1=Label(ventana,text="Escoge una reina").grid(row=0,column=5)
                op1 = 1
            elif carta5p1==64 or carta5p1==65 or carta5p1==66 or carta5p1==67:
                lblp1=Label(ventana,text="Duerme una reina").grid(row=0,column=5)
                op1=2
            elif carta5p1==49 or carta5p1==50 or carta5p1==51 or carta5p1==52:
                lblp1=Label(ventana,text="Roba una reina  ").grid(row=0,column=5)
                op1=3
            elif (carta5p1==58 or carta5p1==59 or carta5p1==60) and op2==2:
                op2=0
            elif (carta5p1==61 or carta5p1==62 or carta5p1==63) and op2==3:
                op2=0
            elif carta5p1==53 or carta5p1==54 or carta5p1==55 or carta5p1==56 or carta5p1==57:
                jk=1
            boton5 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='red',variable=card5p1,onvalue=1,offvalue=0).grid(row=0,column=4)
            carta5p1=vector2[cardsA]
    elif cards>1:
        if c1==1:
            boton1 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='red',variable=card1p1,onvalue=1,offvalue=0).grid(row=0,column=0)
            carta1p1=vector2[cardsB+1]
            cardsB += 1
        if c2==1:
            boton2 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='red',variable=card2p1,onvalue=1,offvalue=0).grid(row=0,column=1)
            carta2p1=vector2[cardsB+1]
            cardsB += 1
        if c3==1:
            boton3 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='red',variable=card3p1,onvalue=1,offvalue=0).grid(row=0,column=2)
            carta3p1=vector2[cardsB+1]
            cardsB += 1
        if c4==1:
            boton4 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='red',variable=card4p1,onvalue=1,offvalue=0).grid(row=0,column=3)
            carta4p1=vector2[cardsB+1]
            cardsB += 1
        if c5==1:
            boton5 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='red',variable=card5p1,onvalue=1,offvalue=0).grid(row=0,column=4)
            carta5p1=vector2[cardsB+1]
    else:
        lblp1=Label(ventana,text="No hay cartas seleccionadas").grid(row=0,column=5)
    if cardsA>=68 and queens1>queens2:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if cardsA>=68 and queens2>queens1:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    if cardsA>=68 and queens2==queens1:
        tkMessageBox.showinfo(title="Juego terminado",message="Empate")

def tirop2():
    global op1
    global op2
    global carta1p1
    global carta2p1
    global carta3p1
    global carta4p1
    global carta5p1
    global carta1p2
    global carta2p2
    global carta3p2
    global carta4p2
    global carta5p2
    global cardsA
    c1=card1p2.get()
    c2=card2p2.get()
    c3=card3p2.get()
    c4=card4p2.get()
    c5=card5p2.get()
    cards = c1+c2+c3+c4+c5
    cardsB = cardsA
    cardsA += cards
    if cards==1:
        if c1==1:
            if carta1p2==41 or carta1p2==42 or carta1p2==43 or carta1p2==44 or carta1p2==45 or carta1p2==46 or carta1p2==47 or carta1p2==48:
                lblp2=Label(ventana,text="Escoge una reina").grid(row=4,column=5)
                op2 = 1
            elif carta1p2==64 or carta1p2==65 or carta1p2==66 or carta1p2==67:
                lblp2=Label(ventana,text="Duerme una reina").grid(row=4,column=5)
                op2=2
            elif carta1p2==49 or carta1p2==50 or carta1p2==51 or carta1p2==52:
                lblp2=Label(ventana,text="Roba una reina  ").grid(row=4,column=5)
                op2=3
            elif (carta1p2==58 or carta1p2==59 or carta1p2==60) and op1==2:
                op1=0
            elif (carta1p2==61 or carta1p2==62 or carta1p2==63) and op1==3:
                op1=0
            elif carta1p2==53 or carta1p2==54 or carta1p2==55 or carta1p2==56 or carta1p2==57:
                jk=1
            boton11 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='blue',variable=card1p2,onvalue=1,offvalue=0).grid(row=4,column=0)
            carta1p2=vector2[cardsA]
        elif c2==1:
            if carta2p2==41 or carta2p2==42 or carta2p2==43 or carta2p2==44 or carta2p2==45 or carta2p2==46 or carta2p2==47 or carta2p2==48:
                lblp2=Label(ventana,text="Escoge una reina").grid(row=4,column=5)
                op2 = 1
            elif carta2p2==64 or carta2p2==65 or carta2p2==66 or carta2p2==67:
                lblp2=Label(ventana,text="Duerme una reina").grid(row=4,column=5)
                op2=2
            elif carta2p2==49 or carta2p2==50 or carta2p2==51 or carta2p2==52:
                lblp2=Label(ventana,text="Roba una reina  ").grid(row=4,column=5)
                op2=3
            elif (carta2p2==58 or carta2p2==59 or carta2p2==60) and op1==2:
                op1=0
            elif (carta2p2==61 or carta2p2==62 or carta2p2==63) and op1==3:
                op1=0
            elif carta2p2==53 or carta2p2==54 or carta2p2==55 or carta2p2==56 or carta2p2==57:
                jk=1
            boton12 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='blue',variable=card2p2,onvalue=1,offvalue=0).grid(row=4,column=1)
            carta2p2=vector2[cardsA]
        elif c3==1:
            if carta3p2==41 or carta3p2==42 or carta3p2==43 or carta3p2==44 or carta3p2==45 or carta3p2==46 or carta3p2==47 or carta3p2==48:
                lblp2=Label(ventana,text="Escoge una reina").grid(row=4,column=5)
                op2 = 1
            elif carta3p2==64 or carta3p2==65 or carta3p2==66 or carta3p2==67:
                lblp2=Label(ventana,text="Duerme una reina").grid(row=4,column=5)
                op2=2
            elif carta3p2==49 or carta3p2==50 or carta3p2==51 or carta3p2==52:
                lblp2=Label(ventana,text="Roba una reina  ").grid(row=4,column=5)
                op2=3
            elif (carta3p2==58 or carta3p2==59 or carta3p2==60) and op1==2:
                op1=0
            elif (carta3p2==61 or carta3p2==62 or carta3p2==63) and op1==3:
                op1=0
            elif carta3p2==53 or carta3p2==54 or carta3p2==55 or carta3p2==56 or carta3p2==57:
                jk=1
            boton13 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='blue',variable=card3p2,onvalue=1,offvalue=0).grid(row=4,column=2)
            carta3p2=vector2[cardsA]
        elif c4==1:
            if carta4p2==41 or carta4p2==42 or carta4p2==43 or carta4p2==44 or carta4p2==45 or carta4p2==46 or carta4p2==47 or carta4p2==48:
                lblp2=Label(ventana,text="Escoge una reina").grid(row=4,column=5)
                op2 = 1
            elif carta4p2==64 or carta4p2==65 or carta4p2==66 or carta4p2==67:
                lblp1=Label(ventana,text="Duerme una reina").grid(row=4,column=5)
                op2=2
            elif carta4p2==49 or carta4p2==50 or carta4p2==51 or carta4p2==52:
                lblp1=Label(ventana,text="Roba una reina  ").grid(row=4,column=5)
                op2=3
            elif (carta4p2==58 or carta4p2==59 or carta4p2==60) and op1==2:
                op1=0
            elif (carta4p2==61 or carta4p2==62 or carta4p2==63) and op1==3:
                op1=0
            elif carta4p2==53 or carta4p2==54 or carta4p2==55 or carta4p2==56 or carta4p2==57:
                jk=1
            boton14 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='blue',variable=card4p2,onvalue=1,offvalue=0).grid(row=4,column=3)
            carta4p2=vector2[cardsA]
        elif c5==1:
            if carta5p2==41 or carta5p2==42 or carta5p2==43 or carta5p2==44 or carta5p2==45 or carta5p2==46 or carta5p2==47 or carta5p2==48:
                lblp2=Label(ventana,text="Escoge una reina").grid(row=4,column=5)
                op2 = 1
            elif carta5p2==64 or carta5p2==65 or carta5p2==66 or carta5p2==67:
                lblp2=Label(ventana,text="Duerme una reina").grid(row=4,column=5)
                op2=2
            elif carta5p2==49 or carta5p2==50 or carta5p2==51 or carta5p2==52:
                lblp2=Label(ventana,text="Roba una reina  ").grid(row=4,column=5)
                op2=3
            elif (carta5p2==58 or carta5p2==59 or carta5p2==60) and op1==2:
                op1=0
            elif (carta5p2==61 or carta5p2==62 or carta5p2==63) and op1==3:
                op1=0
            elif carta5p2==53 or carta5p2==54 or carta5p2==55 or carta5p2==56 or carta5p2==57:
                jk=1
            boton15 = Checkbutton(ventana,image=baraja[vector2[cardsA]],bg='blue',variable=card5p2,onvalue=1,offvalue=0).grid(row=4,column=4)
            carta5p2=vector2[cardsA]
    elif cards>1:
        if c1==1:
            boton11 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='blue',variable=card1p2,onvalue=1,offvalue=0).grid(row=4,column=0)
            carta1p2=vector2[cardsB+1]
            cardsB += 1
        if c2==1:
            boton12 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='blue',variable=card2p2,onvalue=1,offvalue=0).grid(row=4,column=1)
            carta2p2=vector2[cardsB+1]
            cardsB += 1
        if c3==1:
            boton13 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='blue',variable=card3p2,onvalue=1,offvalue=0).grid(row=4,column=2)
            carta3p2=vector2[cardsB+1]
            cardsB += 1
        if c4==1:
            boton14 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='blue',variable=card4p2,onvalue=1,offvalue=0).grid(row=4,column=3)
            carta4p2=vector2[cardsB+1]
            cardsB += 1
        if c5==1:
            boton15 = Checkbutton(ventana,image=baraja[vector2[cardsB+1]],bg='blue',variable=card5p2,onvalue=1,offvalue=0).grid(row=4,column=4)
            carta5p2=vector2[cardsB+1]
    else:
        lblp2=Label(ventana,text="No hay cartas seleccionadas").grid(row=4,column=5)
    if cardsA>=68 and queens1>queens2:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if cardsA>=68 and queens2>queens1:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    if cardsA>=68 and queens2==queens1:
        tkMessageBox.showinfo(title="Juego terminado",message="Empate")


def reina1():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton6q = Button(ventana,image=reinas[vector1[0]],bg='red',command=reina1).grid(row=1,column=0)
        queens1 +=1
    if op1==2:
        boton6q = Button(ventana,image=reinas[vector1[0]],command=reina1).grid(row=1,column=0)
        queens2-=1
    if op1==3:
        boton6q = Button(ventana,image=reinas[vector1[0]],bg='red',command=reina1).grid(row=1,column=0)
        queens1 +=1
    if op2==1:
        boton6q = Button(ventana,image=reinas[vector1[0]],bg='blue',command=reina1).grid(row=1,column=0)
        queens2 +=1
    if op2==2:
        boton6q = Button(ventana,image=reinas[vector1[0]],command=reina1).grid(row=1,column=0)
        queens1-=1
    if op2==3:
        boton6q = Button(ventana,image=reinas[vector1[0]],bg='blue',command=reina1).grid(row=1,column=0)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina2():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton7q = Button(ventana,image=reinas[vector1[1]],bg='red',command=reina2).grid(row=1,column=1)
        queens1 +=1
    if op1==2:
        boton7q = Button(ventana,image=reinas[vector1[1]],command=reina2).grid(row=1,column=1)
        queens2-=1
    if op1==3:
        boton7q = Button(ventana,image=reinas[vector1[1]],bg='red',command=reina2).grid(row=1,column=1)
        queens1 +=1
    if op2==1:
        boton7q = Button(ventana,image=reinas[vector1[1]],bg='blue',command=reina2).grid(row=1,column=1)
        queens2 +=1
    if op2==2:
        boton7q = Button(ventana,image=reinas[vector1[1]],command=reina2).grid(row=1,column=1)
        queens1-=1
    if op2==3:
        boton7q = Button(ventana,image=reinas[vector1[1]],bg='blue',command=reina2).grid(row=1,column=1)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina3():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton8q = Button(ventana,image=reinas[vector1[2]],bg='red',command=reina3).grid(row=1,column=2)
        queens1 +=1
    if op1==2:
        boton8q = Button(ventana,image=reinas[vector1[2]],command=reina3).grid(row=1,column=2)
        queens2-=1
    if op1==3:
        boton8q = Button(ventana,image=reinas[vector1[2]],bg='red',command=reina3).grid(row=1,column=2)
        queens1 +=1
    if op2==1:
        boton8q = Button(ventana,image=reinas[vector1[2]],bg='blue',command=reina3).grid(row=1,column=2)
        queens2 +=1
    if op2==2:
        boton8q = Button(ventana,image=reinas[vector1[2]],command=reina3).grid(row=1,column=2)
        queens1-=1
    if op2==3:
        boton8q = Button(ventana,image=reinas[vector1[2]],bg='blue',command=reina3).grid(row=1,column=2)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina4():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton9q = Button(ventana,image=reinas[vector1[3]],bg='red',command=reina4).grid(row=1,column=3)
        queens1 +=1
    if op1==2:
        boton9q = Button(ventana,image=reinas[vector1[3]],command=reina4).grid(row=1,column=3)
        queens2-=1
    if op1==3:
        boton9q = Button(ventana,image=reinas[vector1[3]],bg='red',command=reina4).grid(row=1,column=3)
        queens1 +=1
    if op2==1:
        boton9q = Button(ventana,image=reinas[vector1[3]],bg='blue',command=reina4).grid(row=1,column=3)
        queens2 +=1
    if op2==2:
        boton9q = Button(ventana,image=reinas[vector1[3]],command=reina4).grid(row=1,column=3)
        queens1-=1
    if op2==3:
        boton9q = Button(ventana,image=reinas[vector1[3]],bg='blue',command=reina4).grid(row=1,column=3)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina5():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton10q = Button(ventana,image=reinas[vector1[4]],bg='red',command=reina5).grid(row=2,column=0)
        queens1 +=1
    if op1==2:
        boton10q = Button(ventana,image=reinas[vector1[4]],command=reina5).grid(row=2,column=0)
        queens2-=1
    if op1==3:
        boton10q = Button(ventana,image=reinas[vector1[4]],bg='red',command=reina5).grid(row=2,column=0)
        queens1 +=1
    if op2==1:
        boton10q = Button(ventana,image=reinas[vector1[4]],bg='blue',command=reina5).grid(row=2,column=0)
        queens2 +=1
    if op2==2:
        boton10q = Button(ventana,image=reinas[vector1[4]],command=reina5).grid(row=2,column=0)
        queens1-=1
    if op2==3:
        boton10q = Button(ventana,image=reinas[vector1[4]],bg='blue',command=reina5).grid(row=2,column=0)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina6():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton11q = Button(ventana,image=reinas[vector1[5]],bg='red',command=reina6).grid(row=2,column=1)
        queens1 +=1
    if op1==2:
        boton11q = Button(ventana,image=reinas[vector1[5]],command=reina6).grid(row=2,column=1)
        queens2-=1
    if op1==3:
        boton11q = Button(ventana,image=reinas[vector1[5]],bg='red',command=reina6).grid(row=2,column=1)
        queens1 +=1
    if op2==1:
        boton11q = Button(ventana,image=reinas[vector1[5]],bg='blue',command=reina6).grid(row=2,column=1)
        queens2 +=1
    if op2==2:
        boton11q = Button(ventana,image=reinas[vector1[5]],command=reina6).grid(row=2,column=1)
        queens1-=1
    if op2==3:
        boton11q = Button(ventana,image=reinas[vector1[5]],bg='blue',command=reina6).grid(row=2,column=1)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina7():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton12q = Button(ventana,image=reinas[vector1[6]],bg='red',command=reina7).grid(row=2,column=2)
        queens1 +=1
    if op1==2:
        boton12q = Button(ventana,image=reinas[vector1[6]],command=reina7).grid(row=2,column=2)
        queens2-=1
    if op1==3:
        boton12q = Button(ventana,image=reinas[vector1[6]],bg='red',command=reina7).grid(row=2,column=2)
        queens1 +=1
    if op2==1:
        boton12q = Button(ventana,image=reinas[vector1[6]],bg='blue',command=reina7).grid(row=2,column=2)
        queens2 +=1
    if op2==2:
        boton12q = Button(ventana,image=reinas[vector1[6]],command=reina7).grid(row=2,column=2)
        queens1-=1
    if op2==3:
        boton12q = Button(ventana,image=reinas[vector1[6]],bg='blue',command=reina7).grid(row=2,column=2)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina8():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton13q = Button(ventana,image=reinas[vector1[7]],bg='red',command=reina8).grid(row=2,column=3)
        queens1 +=1
    if op1==2:
        boton13q = Button(ventana,image=reinas[vector1[7]],command=reina8).grid(row=2,column=3)
        queens2-=1
    if op1==3:
        boton13q = Button(ventana,image=reinas[vector1[7]],bg='red',command=reina8).grid(row=2,column=3)
        queens1 +=1
    if op2==1:
        boton13q = Button(ventana,image=reinas[vector1[7]],bg='blue',command=reina8).grid(row=2,column=3)
        queens2 +=1
    if op2==2:
        boton13q = Button(ventana,image=reinas[vector1[7]],command=reina8).grid(row=2,column=3)
        queens1-=1
    if op2==3:
        boton13q = Button(ventana,image=reinas[vector1[7]],bg='blue',command=reina8).grid(row=2,column=3)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina9():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton14q = Button(ventana,image=reinas[vector1[8]],bg='red',command=reina9).grid(row=3,column=0)
        queens1 +=1
    if op1==2:
        boton14q = Button(ventana,image=reinas[vector1[8]],command=reina9).grid(row=3,column=0)
        queens2-=1
    if op1==3:
        boton14q = Button(ventana,image=reinas[vector1[8]],bg='red',command=reina9).grid(row=3,column=0)
        queens1 +=1
    if op2==1:
        boton14q = Button(ventana,image=reinas[vector1[8]],bg='blue',command=reina9).grid(row=3,column=0)
        queens2 +=1
    if op2==2:
        boton14q = Button(ventana,image=reinas[vector1[8]],command=reina9).grid(row=3,column=0)
        queens1-=1
    if op2==3:
        boton14q = Button(ventana,image=reinas[vector1[8]],bg='blue',command=reina9).grid(row=3,column=0)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina10():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton15q = Button(ventana,image=reinas[vector1[9]],bg='red',command=reina10).grid(row=3,column=1)
        queens1 +=1
    if op1==2:
        boton15q = Button(ventana,image=reinas[vector1[9]],command=reina10).grid(row=3,column=1)
        queens2-=1
    if op1==3:
        boton15q = Button(ventana,image=reinas[vector1[9]],bg='red',command=reina10).grid(row=3,column=1)
        queens1 +=1
    if op2==1:
        boton15q = Button(ventana,image=reinas[vector1[9]],bg='blue',command=reina10).grid(row=3,column=1)
        queens2 +=1
    if op2==2:
        boton15q = Button(ventana,image=reinas[vector1[9]],command=reina10).grid(row=3,column=1)
        queens1-=1
    if op2==3:
        boton15q = Button(ventana,image=reinas[vector1[9]],bg='blue',command=reina10).grid(row=3,column=1)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina11():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton16q = Button(ventana,image=reinas[vector1[10]],bg='red',command=reina11).grid(row=3,column=2)
        queens1 +=1
    if op1==2:
        boton16q = Button(ventana,image=reinas[vector1[10]],command=reina11).grid(row=3,column=2)
        queens2-=1
    if op1==3:
        boton16q = Button(ventana,image=reinas[vector1[10]],bg='red',command=reina11).grid(row=3,column=2)
        queens1 +=1
    if op2==1:
        boton16q = Button(ventana,image=reinas[vector1[10]],bg='blue',command=reina11).grid(row=3,column=2)
        queens2 +=1
    if op2==2:
        boton16q = Button(ventana,image=reinas[vector1[10]],command=reina11).grid(row=3,column=2)
        queens1-=1
    if op2==3:
        boton16q = Button(ventana,image=reinas[vector1[10]],bg='blue',command=reina11).grid(row=3,column=2)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

def reina12():
    global op1
    global op2
    global queens1
    global queens2
    if op1==1:
        boton17q = Button(ventana,image=reinas[vector1[11]],bg='red',command=reina12).grid(row=3,column=3)
        queens1 +=1
    if op1==2:
        boton17q = Button(ventana,image=reinas[vector1[11]],command=reina12).grid(row=3,column=3)
        queens2-=1
    if op1==3:
        boton17q = Button(ventana,image=reinas[vector1[11]],bg='red',command=reina12).grid(row=3,column=3)
        queens1 +=1
    if op2==1:
        boton17q = Button(ventana,image=reinas[vector1[11]],bg='blue',command=reina12).grid(row=3,column=3)
        queens2 +=1
    if op2==2:
        boton17q = Button(ventana,image=reinas[vector1[11]],command=reina12).grid(row=3,column=3)
        queens1-=1
    if op2==3:
        boton17q = Button(ventana,image=reinas[vector1[11]],bg='blue',command=reina12).grid(row=3,column=3)
        queens2 +=1
    op1=0
    op2=0
    if queens1 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador rojo")
    if queens2 == 4:
        tkMessageBox.showinfo(title="Juego terminado",message="El ganador es el jugador azul")
    lblp1=Label(ventana,text="                ").grid(row=0,column=5)
    lblp2=Label(ventana,text="                ").grid(row=4,column=5)

ventana=Tk()
ventana.geometry("750x700+0+0")
ventana.title("Sleeping Queens")
cardsA=9
barajaimg=PhotoImage(file="baraja.gif")
hatking=PhotoImage(file="Hat king.gif")
turtleking=PhotoImage(file="Turtle king.gif")
tidyeking=PhotoImage(file="Tidye king.gif")
puzzleking=PhotoImage(file="Puzzle king.gif")
fireking=PhotoImage(file="Fire king.gif")
cookieking=PhotoImage(file="Cookie king.gif")
chessking=PhotoImage(file="Chess king.gif")
bubbleking=PhotoImage(file="Bubble king.gif")
a1=PhotoImage(file="1.gif")
a2=PhotoImage(file="2.gif")
a3=PhotoImage(file="3.gif")
a4=PhotoImage(file="4.gif")
a5=PhotoImage(file="5.gif")
a6=PhotoImage(file="6.gif")
a7=PhotoImage(file="7.gif")
a8=PhotoImage(file="8.gif")
a9=PhotoImage(file="9.gif")
a10=PhotoImage(file="10.gif")
knight1=PhotoImage(file="01.gif")
knight2=PhotoImage(file="02.gif")
knight3=PhotoImage(file="03.gif")
knight4=PhotoImage(file="04.gif")
joker1=PhotoImage(file="joker.gif")
potion1=PhotoImage(file="Potion.gif")
varita1=PhotoImage(file="Varita.gif")
dragon1=PhotoImage(file="Dragon.gif")
cat=PhotoImage(file="cat.gif")
cake=PhotoImage(file="Cake.gif")
dog=PhotoImage(file="dog.gif")
heart=PhotoImage(file="Heart.gif")
ladybug=PhotoImage(file="Ladybug.gif")
moon=PhotoImage(file="moon.gif")
peacock=PhotoImage(file="Peacock.gif")
pancake=PhotoImage(file="Pancake.gif")
rainbow=PhotoImage(file="Rainbow.gif")
rose=PhotoImage(file="Rose.gif")
starfish=PhotoImage(file="Starfish.gif")
sunflower=PhotoImage(file="Sunflower.gif")
b1=a1
b2=a2
b3=a3
b4=a4
b5=a5
b6=a6
b7=a7
b8=a8
b9=a9
b10=a10
c1=a1
c2=a2
c3=a3
c4=a4
c5=a5
c6=a6
c7=a7
c8=a8
c9=a9
c10=a10
d1=a1
d2=a2
d3=a3
d4=a4
d5=a5
d6=a6
d7=a7
d8=a8
d9=a9
d10=a10
joker2=joker1
joker3=joker1
joker4=joker1
joker5=joker1
dragon2=dragon1
dragon3=dragon1
potion2=potion1
potion3=potion1
potion4=potion1
varita2=varita1
varita3=varita1
reinas=[0,cat,cake,dog,heart,ladybug,moon,peacock,pancake,rainbow,rose,starfish,sunflower]
baraja=[0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,hatking,turtleking,tidyeking,puzzleking,fireking,bubbleking,chessking,cookieking,knight1,knight2,knight3,knight4,joker1,joker2,joker3,joker4,joker5,varita1,varita2,varita3,dragon1,dragon2,dragon3,potion1,potion2,potion3,potion4]
vector1=[0,0,0,0,0,0,0,0,0,0,0,0]
vector2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
card1p1=IntVar()
card2p1=IntVar()
card3p1=IntVar()
card4p1=IntVar()
card5p1=IntVar()
card1p2=IntVar()
card2p2=IntVar()
card3p2=IntVar()
card4p2=IntVar()
card5p2=IntVar()
op1=0
op2=0
queens1=0
queens2=0

for a in range(0,12):
    while True:
        cartas = random.randint(1,12)
        stop=0
        for b in range(0,12):
            if vector1[b] == cartas:
                stop=1
        if stop==0:
            break
    vector1[a]= cartas
for a in range(0,67):
    while True:
        cartas = random.randint(1,67)
        stop=0
        for b in range(0,67):
            if vector2[b] == cartas:
                stop=1
        if stop==0:
            break
    vector2[a]= cartas

boton1 = Checkbutton(ventana,image=baraja[vector2[0]],bg='red',variable=card1p1,onvalue=1,offvalue=0).grid(row=0,column=0)
boton2 = Checkbutton(ventana,image=baraja[vector2[1]],bg='red',variable=card2p1,onvalue=1,offvalue=0).grid(row=0,column=1)
boton3 = Checkbutton(ventana,image=baraja[vector2[2]],bg='red',variable=card3p1,onvalue=1,offvalue=0).grid(row=0,column=2)
boton4 = Checkbutton(ventana,image=baraja[vector2[3]],bg='red',variable=card4p1,onvalue=1,offvalue=0).grid(row=0,column=3)
boton5 = Checkbutton(ventana,image=baraja[vector2[4]],bg='red',variable=card5p1,onvalue=1,offvalue=0).grid(row=0,column=4)
carta1p1 = vector2[0]
carta2p1 = vector2[1]
carta3p1 = vector2[2]
carta4p1 = vector2[3]
carta5p1 = vector2[4]
carta1p2 = vector2[5]
carta2p2 = vector2[6]
carta3p2 = vector2[7]
carta4p2 = vector2[8]
carta5p2 = vector2[9]

boton6q = Button(ventana,image=reinas[vector1[0]],command=reina1).grid(row=1,column=0)
boton7q = Button(ventana,image=reinas[vector1[1]],command=reina2).grid(row=1,column=1)
boton8q = Button(ventana,image=reinas[vector1[2]],command=reina3).grid(row=1,column=2)
boton9q = Button(ventana,image=reinas[vector1[3]],command=reina4).grid(row=1,column=3)
boton10q = Button(ventana,image=reinas[vector1[4]],command=reina5).grid(row=2,column=0)
boton11q = Button(ventana,image=reinas[vector1[5]],command=reina6).grid(row=2,column=1)
boton12q = Button(ventana,image=reinas[vector1[6]],command=reina7).grid(row=2,column=2)
boton13q = Button(ventana,image=reinas[vector1[7]],command=reina8).grid(row=2,column=3)
boton14q = Button(ventana,image=reinas[vector1[8]],command=reina9).grid(row=3,column=0)
boton15q = Button(ventana,image=reinas[vector1[9]],command=reina10).grid(row=3,column=1)
boton16q = Button(ventana,image=reinas[vector1[10]],command=reina11).grid(row=3,column=2)
boton17q = Button(ventana,image=reinas[vector1[11]],command=reina12).grid(row=3,column=3)

botonP1 = Button(ventana,text="Tirar",command=tirop1).grid(row=1,column=4)
botonBaraja = Button(ventana,image=barajaimg).grid(row=2,column=4)
botonP2 = Button(ventana,text="Tirar",command=tirop2).grid(row=3,column=4)

boton11 = Checkbutton(ventana,image=baraja[vector2[5]],bg='blue',variable=card1p2,onvalue=1,offvalue=0).grid(row=4,column=0)
boton12 = Checkbutton(ventana,image=baraja[vector2[6]],bg='blue',variable=card2p2,onvalue=1,offvalue=0).grid(row=4,column=1)
boton13 = Checkbutton(ventana,image=baraja[vector2[7]],bg='blue',variable=card3p2,onvalue=1,offvalue=0).grid(row=4,column=2)
boton14 = Checkbutton(ventana,image=baraja[vector2[8]],bg='blue',variable=card4p2,onvalue=1,offvalue=0).grid(row=4,column=3)
boton15 = Checkbutton(ventana,image=baraja[vector2[9]],bg='blue',variable=card5p2,onvalue=1,offvalue=0).grid(row=4,column=4)

lblp1=Label(ventana,text="").grid(row=0,column=5)
lblpp=Label(ventana,text="").grid(row=1,column=5)
lblchoose=Label(ventana,text="").grid(row=2,column=5)
lblppp=Label(ventana,text="").grid(row=3,column=5)
lblp2=Label(ventana,text="").grid(row=4,column=5)

ventana.mainloop()