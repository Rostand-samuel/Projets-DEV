#ici on importe nos bibliotheques

from cProfile import label
from subprocess import call
from tkinter import ttk, Tk
from tkinter import*
from tkinter import messagebox
#from tkinter.tix import ButtonBox
#from webbrowser import BackgroundBrowser
import mysql.connector



#l'interface pour les commades

root = Tk()
root.title("RESTO-ROST")
root.geometry("1200x700+2+20")
root.resizable(False,False)
root.configure(background="#164159")


#Formulaire d'enregistrement des commandes
lbl_titre = Label(root
, text = "Formulaire  des commandes", 
font=("Sans Serif",16), background = "purple", foreground ="white")
lbl_titre.place(x=5,y=20, width=400)

lbl_aliment = Label(root,  text ="Code Aliment", font=("Sana Serif",13), background="#164159", foreground ="white")
lbl_aliment.place(x=10,y=70, width=300)

txt_aliment=Entry(root, bd = 4, font=("Arial",14))
txt_aliment.place(x=260,y=70, width=150)


lbl_quantite = Label(root,  text ="Quantite", font=("Sana Serif",13), background="#164159", foreground ="white")
lbl_quantite.place(x=10,y=120, width=300)
txt_quantite=Entry(root, bd = 4, font=("Arial",14))
txt_quantite.place(x=260,y=120, width=150)

lbl_num_table = Label(root,  text ="Numero Table", font=("Sana Serif",13), background="#164159", foreground ="white")
lbl_num_table.place(x=10,y=170, width=300)
txt_num_table=Entry(root, bd = 4, font=("Arial",14))
txt_num_table.place(x=260,y=170, width=150)

#les boutons d'achats

btn_enregistrer_Table = Button(root, text="ENREGISTRER", font=("Arial",15), bg="green", fg="white")
btn_enregistrer_Table.place(x=50,y=230,width=180)

btn_annuler_Table = Button(root, text="ANNULER", font=("Arial",15), bg="yellow", fg="black")
btn_annuler_Table.place(x=50,y=285,width=180)

txt_annuler=Entry(root, bd = 4, font=("Arial",14))
txt_annuler.place(x=260,y=285, width=150, height=40)

btn_liberer_Table = Button(root, text="LIBERER UNE TABLE", font=("Arial",15), bg="skyblue", fg="white")
btn_liberer_Table.place(x=50,y=335,width=280)

#
lbl_titre = Label(root
, text = "MONTANTS TOTAUX", 
font=("Sans Serif",16), background = "purple", foreground ="white")
lbl_titre.place(x=5,y=400, width=400)

#creer la table 
table = ttk.Treeview(root, columns=(1,2,3,4), height=10, show="headings")
table.place(x=500, y=60,width=600, height=600)

#Entete
table.heading(1, text="Id COMMANDE")
table.heading(2, text="NUMERO TABLE")
table.heading(3, text="COMMANDE")
table.heading(4, text="QUANTITE")

#definir les dimensions des colonnes
table.column(1,width=50)
table.column(2,width=50)
table.column(3,width=100)
table.column(4,width=100)

#creer la table des montants
table = ttk.Treeview(root, columns=(1,2), height=10, show="headings")
table.place(x=10, y=450,width=400, height=200)

#Entete
table.heading(1, text="NUMERO TABLE")
table.heading(2, text="MONTANT")


#definir les dimensions des colonnes
table.column(1,width=50)
table.column(2,width=50)




#executeur
root.mainloop()