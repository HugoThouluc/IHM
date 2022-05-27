import string
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from pynput.keyboard import Key, Controller
from PIL import Image, ImageTk 
import serial
import time
from tkinter import messagebox

w = Tk()  # Créer une fenêtre

############################# UART #############################

port='/dev/ttyUSB0'
baudrate=115200
serBuffer = ""

ser = serial.Serial(port, baudrate, bytesize=8, parity='N', stopbits=1, timeout=None, rtscts=False, dsrdtr=False)

############################# FONCTIONS #############################

#Envoie texte vers fichier
def click_envoyer():
    fichier = open("fichier.txt", "w")
    fichier.write(entry_envoyer.get())
    messagebox.showinfo(title=None, message='Message envoyé')
    fichier.close()


#Envoie fichier vers texte
def click_recevoir():
    fichier = open("fichier.txt", "r")
    content = fichier.readline()
    label_text2.configure(text=content)
    fichier.close()

#Graphe
def courbe():
    x = 0
    for i in range(100):
        x = x+0.04
        #fonction = entry_function.get()
        '''for i in range(int(fonction)):
            if fonction[i] == "0":
                number = 0
            if fonction[i] == '1':
                number = 1
            if fonction[i] == '2':
                number = 2
            if fonction[i] == '3':
                number = 3
            if fonction[i] == '4':
                number = 4
            if fonction[i] == '5':
                number = 5
            if fonction[i] == '6':
                number = 6
            if fonction[i] == '7':
                number = 7
            if fonction[i] == '8':
                number = 8
            if fonction[i] == '9':
                number = 9
            if fonction[i] == 'x':
                y = number*x
            if fonction[i] == '+':
                y = number+x
            if fonction[i] == '-':
                y = number-x
            if fonction[i] == '/':
                y = number/x
            if fonction[0] == 's':
                y = np.sin(x)
            if fonction[0] == 'c':
                y = np.cos(x)
            if fonction[0] == 't':
                y = np.tan(x)'''
        y = np.sin(x)
        plt.scatter(x,y)
        plt.title("Courbe en temps réel")
        plt.xlabel("x")
        plt.ylabel("sin(x)")
        plt.pause(0.01)

#CSV vers texte
def click_Recevoir_csv():
    with open ("fichierCSV.csv","r") as file:
        label_csv = Label(w, text=file.read(), bg="white", font=("Arial",13))
        label_csv.place(x=100,y=350)

#texte vers CSV
def click_Envoyer_csv():
    test_csv_send = text_csv.get("1.0", "end")
    text_csv.delete("1.0", "end")
    with open("fichierCSV.csv", 'w') as file :
        file.write(test_csv_send + "\n")
        file.close()
    messagebox.showinfo(title=None, message='Message envoyé')

def avance():
    var = 'z' 
    ser.write(var.encode())

def recule():
    var = 's' 
    ser.write(var.encode())

def droite():
    var = 'd' 
    ser.write(var.encode())

def gauche():
    var = 'q' 
    ser.write(var.encode())

def stop():
    var = 'p' 
    ser.write(var.encode())
    

# Personnalisation de la fenêtre
w.title("Interface Homme Machine") #Titre
w.geometry("750x600") #Taille
w.minsize(750, 600)
#w.iconbitmap("ENIB.ico") #Logo icone
w.config(background='white')

frame = Frame(w, bg='white')

c = Canvas(w, height=600, width=720, highlightthickness=0, bg='white')
c.place(x=0, y=0)

rectangleIHM = c.create_rectangle(530,30,710,170, width=1)
rectangletexte = c.create_rectangle(30,5,490,180, width=1)
rectangleCSV = c.create_rectangle(30,260,710,530, width=1)

############################# TEXTE #############################

# Insérer un texte
label_text1 = Label(w, text="Texte à envoyer :", font=("Arial",10), bg='white')
label_text1.place(x=50, y=20)

#Zone de texte envoyer
entry_envoyer = Entry(w, font=("Arial"), bg='white')
entry_envoyer.place(x=50,y=50)

#Bouton Envoyer
send_button = Button(w, text="Envoyer", font=("Arial", 20), bg='blue', fg='white', command=click_envoyer)
send_button.place(x=350,y=35)

#Zone de texte recevoir
label_text2 = Label(w, font=("Arial",15), bg='white')
label_text2.place(x=50, y=120)

#Bouton recevoir
receive_button = Button(w, text="Recevoir", font=("Arial", 20), bg='blue', fg='white', command=click_recevoir)
receive_button.place(x=345,y=110)

############################# GRAPHE #############################

#Graphe fonction
entry_function = Entry(w, font=("Arial"), bg='white')
entry_function.place(x=130,y=205)

#Bouton Graphe
graph_button = Button(w, text="Graphe", font=("Arial", 20), bg='blue', fg='white', command=courbe)
graph_button.place(x=351,y=195)

############################# CSV #############################

#Bouton CSV Recevoir
csv_receive_button = Button(w, text="Recevoir", font=("Arial", 20), bg='blue', fg='white', command=click_Recevoir_csv)
csv_receive_button.place(x=150,y=270)

#Bouton CSV Envoyer
csv_send_button = Button(w, text="Envoyer", font=("Arial", 20), bg='blue', fg='white', command=click_Envoyer_csv)
csv_send_button.place(x=450,y=270)

label_textcsv = Label(w, font=("Arial",15), bg='white')
label_textcsv.place(x=100, y=200)

text_csv = Text(w, height=10, width=45, bg='white')
text_csv.place(x=340, y=350)

#Image STAM
imageLogo = PhotoImage(file='Logo_STAM.png')
labelImage = Label(w, image=imageLogo,bg='white')
labelImage.place(x=560,y=177)

############################# IHM ROBOT #############################

copyZ=Button(w, text="Z", font=("Arial",15, "bold"), bg="blue", fg="white", bd=3, relief=RAISED, height=1, width=2, command=avance)
copyZ.place(x=593,y=73)

copyQ=Button(w, text="Q", font=("Arial",15, "bold"), bg="blue", fg="white", bd=3, relief=RAISED, height=1, width=2, command=gauche)
copyQ.place(x=540,y=115)

copyS=Button(w, text="S", font=("Arial",15, "bold"), bg="blue", fg="white", bd=3, relief=RAISED, height=1, width=2, command=recule)
copyS.place(x=593,y=115)

copyD=Button(w, text="D", font=("Arial",15, "bold"), bg="blue", fg="white", bd=3, relief=RAISED, height=1, width=2, command=droite)
copyD.place(x=646,y=115)

copyP=Button(w, text="STOP", font=("Arial",8, "bold"), bg="blue", fg="white", bd=3, relief=RAISED, command=stop)
copyP.place(x=640,y=35)


w.mainloop()  # Affiche la fenêtre

