#ici on importe nos bibliotheques

#from cProfile import label
from subprocess import call
from tkinter import ttk, Tk
from tkinter import*
from tkinter import messagebox
#from tkinter.tix import ButtonBox
#from webbrowser import BackgroundBrowser
import mysql.connector




#la fonction permettant d'ajouter une Table 

def ajouterTable():
    #variable_de_recuperation = nom_variable_de_recuperation.get()
    numero_table = txt_table.get()# pour recuperer l'information que l'utilisateur va entrer
    nombre_chaise = txt_chaise.get()# pour recuperer l'information que l'utilisateur va entrer
    etat = "Libre"
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Restaurant_Python")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO table_restos (numero_table,nombre_chaise,etat) VALUES (%s,%s,%s)"
        val = (numero_table, nombre_chaise, etat)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("information", " Table ajoutee avec succes!")
        #root.destroy()
        call(["python", "Table_aliments.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()




#la fonction permettant de supprimer une Table 

def supprimerTable():
    #variable_de_recuperation = nom_variable_de_recuperation.get()
    numero_table = txt_table.get()# pour recuperer l'information que l'utilisateur va entrer
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Restaurant_Python")
    meConnect = maBase.cursor()

    try:
        sql = "DELETE from table_restos where numero_table =%s"
        val = (numero_table,)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("information", " Table supprimee avec succes!")
        root.destroy()
        call(["python", "Table_aliments.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()




#la fonction permettant d'ajouter un aliment

def ajouterAliment():
    #variable_de_recuperation = nom_variable_de_recuperation.get()
    code_aliment = txt_code_aliment.get()# pour recuperer l'information que l'utilisateur va entrer
    nom_aliment = txt_nom_aliment.get()# pour recuperer l'information que l'utilisateur va entrer
    prix_aliment = txt_prix_aliment.get()# pour recuperer l'information que l'utilisateur va entrer
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Restaurant_Python")
    meConnect = maBase.cursor()

    try:
        sql = "INSERT INTO aliment_resto (code_aliment,nom_aliment,prix_aliment) VALUES (%s,%s,%s)"
        val = (code_aliment, nom_aliment, prix_aliment)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("information", " Aliment ajoutee avec succes!")
        root.destroy()
        call(["python", "Table_aliments.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()




#la fonction permettant de supprimer un Aliment

def supprimerAliment():
    #variable_de_recuperation = nom_variable_de_recuperation.get()
    code_aliment = txt_code_aliment.get()# pour recuperer l'information que l'utilisateur va entrer
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Restaurant_Python")
    meConnect = maBase.cursor()

    try:
        sql = "DELETE from aliment_resto where code_aliment =%s"
        val = (code_aliment,)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("information", " Aliment supprimee avec succes!")
        root.destroy()
        call(["python", "Table_aliments.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()





#l'interface d'acceuil

root = Tk()
root.title("RESTO-ROST")
root.geometry("1200x700+2+20")
root.resizable(False,False)
root.configure(background="orange")


#Formulaire d'enregistrement des tables
lbl_titre = Label(root
, text = "Formulaire d'enregistrement des tables", 
font=("Sans Serif",16), background = "purple", foreground ="white")
lbl_titre.place(x=5,y=20, width=500)

lbl_table = Label(root,  text ="Numero de table", font=("Sana Serif",13), background="orange", foreground ="black")
lbl_table.place(x=10,y=70, width=300)

txt_table=Entry(root, bd = 4, font=("Arial",14))
txt_table.place(x=260,y=70, width=150)


lbl_chaise = Label(root,  text ="Nombre de chaise", font=("Sana Serif",13), background="orange", foreground ="black")
lbl_chaise.place(x=10,y=120, width=300)
txt_chaise=Entry(root, bd = 4, font=("Arial",14))
txt_chaise.place(x=260,y=120, width=150)

#les boutons d'achats

btn_enregistrer_Table = Button(root, text="ENREGISTRER", font=("Arial",15), bg="green", fg="white", command=ajouterTable)
btn_enregistrer_Table.place(x=50,y=190,width=180)

btn_supprimer_Table = Button(root, text="SUPPRIMER", font=("Arial",15), bg="red", fg="white", command=supprimerTable)
btn_supprimer_Table.place(x=260,y=190,width=150)

#creer la table 
table = ttk.Treeview(root, columns=(1,2,3), height=10, show="headings")
table.place(x=550, y=60,width=600, height=200)

#Entete
table.heading(1, text="NUMERO TABLE")
table.heading(2, text="NOMBRE DE CHAISE")
table.heading(3, text="ETAT")

#definir les dimensions des colonnes
table.column(1,width=50)
table.column(2,width=50)
table.column(3,width=100)




#afficher les informations de la table
maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Restaurant_Python")
meConnect = maBase.cursor()
meConnect.execute("select * from table_restos")
for row in meConnect:
    table.insert('', END, values=row)
maBase.close()




#Formulaire d'enregistrement des aliments
lbl_titre_Aliment = Label(root
, text = "Formulaire d'enregistrement des aliments", 
font=("Sans Serif",16), background = "purple", foreground ="white")
lbl_titre_Aliment.place(x=5,y=320, width=500)

lbl_code_aliment = Label(root,  text ="Code aliment", font=("Sana Serif",13), background="orange", foreground ="black")
lbl_code_aliment.place(x=10,y=360, width=300)

txt_code_aliment=Entry(root, bd = 4, font=("Arial",14))
txt_code_aliment.place(x=260,y=360, width=150)


lbl_nom_aliment = Label(root,  text ="Nom aliment", font=("Sana Serif",13), background="orange", foreground ="black")
lbl_nom_aliment.place(x=10,y=410, width=300)
txt_nom_aliment=Entry(root, bd = 4, font=("Arial",14))
txt_nom_aliment.place(x=260,y=410, width=250)

lbl_prix_aliment = Label(root,  text ="Prix aliment", font=("Sana Serif",13), background="orange", foreground ="black")
lbl_prix_aliment.place(x=10,y=465, width=300)
txt_prix_aliment=Entry(root, bd = 4, font=("Arial",14))
txt_prix_aliment.place(x=260,y=465, width=100)

#les boutons d'achats

btn_enregistrer_aliment = Button(root, text="ENREGISTRER", font=("Arial",15), bg="green", fg="white", command=ajouterAliment)
btn_enregistrer_aliment.place(x=50,y=520,width=180)

btn_supprimer_aliment = Button(root, text="SUPPRIMER", font=("Arial",15), bg="red", fg="white", command=supprimerAliment)
btn_supprimer_aliment.place(x=260,y=520,width=150)


btn_commander_aliment = Button(root, text="COMMANDES", font=("Arial",15), bg="blue", fg="white")
btn_commander_aliment.place(x=130,y=575,width=150)

#creer la table aliment
table_aliment = ttk.Treeview(root, columns=(1,2,3), height=10, show="headings")
table_aliment.place(x=550, y=345,width=600, height=300)

#Entete
table_aliment.heading(1, text="CODE ALIMENT")
table_aliment.heading(2, text="NOM ALIMENT")
table_aliment.heading(3, text="PRIX ALIMENT")

#definir les dimensions des colonnes
table_aliment.column(1,width=50)
table_aliment.column(2,width=50)
table_aliment.column(3,width=100)


#afficher les informations des aliments
maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Restaurant_Python")
meConnect = maBase.cursor()
meConnect.execute("select * from aliment_resto")
for row in meConnect:
    table_aliment.insert('', END, values=row)
maBase.close()


#executeur
root.mainloop()