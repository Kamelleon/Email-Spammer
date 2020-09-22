from tkinter import *
from tkinter.scrolledtext import ScrolledText
import smtplib
import os
from email.mime.multipart import MIMEMultipart
import random

def send_mail():
    number_of_mails=int(number_of_mails_entry.get())
    how_many=number_of_mails
    for i in range(how_many):
            server = smtplib.SMTP(mailbox, 587)
            server.ehlo()
            server.starttls()
            # Set message content
            message = 'Subject: {}\n\n{}'.format(random.sample(range(100),7), random.sample(range(100),40))
            # Login to mailbox
            server.login(sender_login, sender_password)
            # Send mails to target
            server.sendmail(sender_login, reciever_mailbox, message)

def save_info(send_mail):
    global sender_label
    sender_label = sender_entry.get()
    global sender_login
    sender_login = sender_label
    global password
    password = password.get()
    global sender_password
    sender_password = password
    global reciever
    reciever = receiver_box.get()
    global reciever_mailbox
    reciever_mailbox = reciever
    global number_of_mails
    number_of_mails=int(number_of_mails_entry.get())
    global how_many
    how_many=number_of_mails

# Onet mailbox button
def omailboxchoose(send_mail):
    global onet
    onet = 'smtp.poczta.onet.pl'
    global  mailbox
    mailbox=onet
# Gmail mailbox button
def gmailboxchoose(send_mail):
    global gmail
    gmail = 'smtp.gmail.com'
    global mailbox
    mailbox=gmail
# Interia mailbox button
def imailboxchoose(send_mail):
    global interia
    interia = 'poczta.interia.pl'
    global mailbox
    mailbox = interia

# Create window
window = Tk()
# Window title
window.title("Email spammer")
# Window size
window.geometry('500x470')

# Mailbox label
mailbox=Label(text='Choose your mailbox:')
mailbox.place(relx=0.25,rely=0.03,relwidth=0.5)
# Onet mailbox button
onet_mailbox=Button(text='ONET', bg='#FFD102', command=lambda:omailboxchoose(send_mail))
onet_mailbox.place(relx=0.20, rely=0.07, relwidth=0.2, relheight = 0.06)
# Gmail mailbox button
gmail_mailbox=Button(text='GMAIL', bg='#F14436', command=lambda:gmailboxchoose(send_mail))
gmail_mailbox.place(relx=0.40, rely=0.07, relwidth=0.2, relheight = 0.06)
# Interia mailbox button
interia_mailbox=Button(text='INTERIA', bg='#3DA3DB', command=lambda:imailboxchoose(send_mail))
interia_mailbox.place(relx=0.60, rely=0.07, relwidth=0.2, relheight = 0.06)
# Login label
sender_label = Label(text = "Login")
sender_label.place(relx=0.25, rely = 0.15, relwidth=0.5 )
# Login entry
sender_entry = Entry(font = 20)
sender_entry.place(relx=0.25, rely = 0.2, relwidth=0.5)
# Password label
sender_password = Label(text = "Password")
sender_password.place(relx=0.25, rely=0.25, relwidth=0.5)
# Password entry
password = Entry(font = 20, show="*")
password.place(relx = 0.25, rely = 0.30, relwidth = 0.5)
# Number of mails label
number_of_mails=Label(text="Number of mails:")
number_of_mails.place(relx=0.25, rely=0.35, relwidth=0.5)
# Number of mails entry
number_of_mails_entry=Entry(font=20)
number_of_mails_entry.place(relx=0.46,rely=0.40, relwidth=0.07)
# Target email label
receiver = Label(text = "Target email:")
receiver.place(relx = 0.4, rely = 0.49, relwidth=0.2)
# Target email entry
receiver_box = Entry(font = 20)
receiver_box.place(relx = 0.25, rely = 0.53, relwidth = 0.5)
# Save button
save=Button(text='SAVE',bg='red',fg='white', command=lambda:save_info(send_mail))
save.place(relx=0.35, rely=0.63, relwidth=0.3)
# SPAM button
button_send = Button(text = "SPAM", bg = "green", fg = "white", command = lambda:send_mail())
button_send.place(relx = 0.25, rely = 0.8, relheight=0.1, relwidth=0.5)

window.mainloop()
