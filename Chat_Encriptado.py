from tkinter import *

login_window = Tk()

login_window.geometry("450x300")
login_window.title("Iniciar Sesión")
login_window.config(background="khaki")

userName = Label(login_window,text="Nombre de Usuario: ", font=("Arial", 13, "bold"), bg="khaki")
userName.place(relx=0.2,rely=0.3,anchor=CENTER)

userName_Entry = Entry(login_window)
userName_Entry.place(relx=0.51,rely=0.3,anchor=CENTER)

yourCode = Label(login_window,text="Código de tu Sala: ", font=("Arial", 13, "bold"), bg="khaki")
yourCode.place(relx=0.187,rely=0.4,anchor=CENTER)

yourCode_Entry = Entry(login_window, width=22)
yourCode_Entry.place(relx=0.497,rely=0.4,anchor=CENTER)

FriendsCode = Label(login_window,text="Código de Amigo: ", font=("Arial", 13, "bold"), bg="khaki")
FriendsCode.place(relx=0.18,rely=0.5,anchor=CENTER)

FriendsCode_Entry = Entry(login_window, width=23)
FriendsCode_Entry.place(relx=0.49,rely=0.5,anchor=CENTER)

btn_start = Button(login_window, text="Enviar", bg="SpringGreen2", width="15", height="2", font=("Arial", 12, "bold"), fg="orange red")
btn_start.place(relx=0.198,rely=0.64,anchor=CENTER)

login_window.mainloop()