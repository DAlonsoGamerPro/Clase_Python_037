from tkinter import *
from firebase import firebase
from simplecrypt import encrypt,decrypt

firebase = firebase.FirebaseApplication("Tu enlace de la Base de Datos",None)
login_window = Tk()

login_window.geometry("450x300")
login_window.title("Iniciar Sesión")
login_window.config(background="khaki")

username = ""
your_code = ""
your_friends_code = ""
message_text = ""
message_entry = ""
last_value = ""

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

def EnterRoom():
    global username
    global your_code
    global your_friends_code
    global message_entry
    global message_text
    
    your_friends_code = FriendsCode_Entry.get()
    your_code = yourCode_Entry.get()
    username = userName_Entry.get()
    
    message_window = Tk()
    message_window.geometry("600x500")
    message_window.title("Sala de Mensajes")
    message_window.config(background="orchid1")
    
    message_text = Text(message_window,height=20,width=72)
    message_text.place(relx=0.5,rely=35,anchor=CENTER)
    
    message_label = Label(message_window,text="Mensaje",background="orchid1", font=("Arial",13))
    message_label.place(relx=0.3,rely=0.8,anchor=CENTER)
    
    message_entry = Entry(message_window,font="arial 13")
    message_entry.place(relx=0.6,rely=0.8,anchor=CENTER)
    
    btn_send = Button(message_window,text="Envíar", font = "arial 13", bg="PaleGreen1", padx=10,relief=FLAT,command=sendData)
    btn_send.place(relx=0.5,rely=0.9,anchor=CENTER)
    
    login_window.destroy()
    message_window.mainloop()

btn_start = Button(login_window, text="Enviar", bg="SpringGreen2", width="15", height="2", font=("Arial", 12, "bold"), fg="orange red", command=EnterRoom)
btn_start.place(relx=0.198,rely=0.64,anchor=CENTER)

login_window.mainloop()
