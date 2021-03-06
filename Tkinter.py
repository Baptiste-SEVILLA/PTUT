import tkinter
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk

fenetre = Tk()


#Liste youtubeurs
Liste = ttk.Combobox(fenetre, values=["Squeezie", "Cyprien", "Norman", "Amixem"])
Liste.pack ()

#Ajout / affichage liste
def print_file () :
    print(Liste.get()) #bouton fleche

#ajouter a la liste
bListe = tkinter.Button (fenetre, text="Ajouter")
bListe.config (command = print_file)         # idem
bListe.pack ()


# bouton de sortie
bFermer=Button(fenetre, text="Fermer", command=fenetre.quit)
bFermer.pack()


# checkbutton
b3 = Checkbutton(fenetre, text="Nouveau?")
b3.pack()


# radiobutton
value = StringVar()
b4 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
b5 = Radiobutton(fenetre, text="Non", variable=value, value=2)
b4.pack()
b5.pack()


# liste
#liste = Listbox(fenetre)
#liste.insert(1, "Python")
#liste.insert(2, "PHP")
#liste.insert(3, "jQuery")
#liste.insert(4, "CSS")
#liste.insert(5, "Javascript")

#liste.pack()


#incrementeur
s = Spinbox(fenetre, from_=0, to=10)
s.pack()


#couleur
# p = PanedWindow(fenetre, orient=HORIZONTAL)
# p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
# p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
# p.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )
# p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )
# p.pack()

#Action
def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
        showerror('Titre3', 'Tout est détruit maintenant')
    else:
        showinfo('Titre 4', 'Vous avez peur!')
        showerror("Titre 5", "Aha")

Button(text='Action', command=callback).pack()


#Barre du menu
def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

#Recuperer Input
def recupere():
    showinfo("Alerte", entree.get())

value = StringVar()
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre, text="Valider", command=recupere)
bouton.pack()


#Frame
fenetre['bg']='white'
# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=10, pady=10)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3
Frame3 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame3.pack(side=LEFT, padx=10, pady=10)
# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)




fenetre.mainloop()  # idem

#Affichage interface graphique