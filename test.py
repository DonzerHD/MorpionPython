from tkinter import *

fenetre = Tk()
fenetre.title('Tkinter tutoriel')
fenetre['bg'] = 'red'

photo = PhotoImage(file="unnamed.png")
label = Label(fenetre, image=photo)
label.place(x= '50', y="50")

fenetre.mainloop()
