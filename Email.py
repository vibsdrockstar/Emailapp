from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import satplib
import os

def start_spam(*args):
    try:
        login_user = str(username.get())
        login_pass = str(password.get())
        spam=int(spam_amount.get())
        msg= str(message.get())
        victim= str(to_adreess.get())
        
        
      while spam > 0:
        server = smtplib.SMTP("smtp.live.com",587)
        server.echlo()
        server.starttls()
        server.sendmail(login_user,victim,msg)
        server.quit

    messagebox.showinfo("Complete!", "Victim has successfully been sent {0} emails!".format(spam))
    os.exit(1)

        except smtplib.SMTPException:
            spam =0
            messagebox.showerror("Error Sending!")
    
           except smtplib.SMTPServerDisconnected
              spam =0
              messagebox.showerror("Error")


root = Tk()
root.simple("Simple email spamming app!")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )

mainframe = ttk.Frame(root, paddling=*4 4 16 16)
mainframe.grid(column= 0, row=0, sticky=(N,W,W,S)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

username = StringVar()
passcode =StringVar()
spam_amount= IntVar()
to_address =StringVar()
message = StringVar()
               
#Entrys
username_entry = ttk.Entry(mainframe, width=10, textvariable=username)
username_entry.grid(column=2, row=1, stick=W)
               
password_entry = ttk.Entry(mainframe, width=10, textvariable=password)
password_entry.grid(column=2, row=1, stick=W)
               
message_entry = ttk.Entry(mainframe, width=15, textvariable=message)
message_entry.grid(column=2, row=3, stick=W)

spam_entry = ttk.Entry(mainframe, width=10, textvariable=spam_amount)
spam_entry.grid(column=2, row=4, stick=W)

to_address_entry = ttk.Entry(mainframe, width=10, textvariable=to_address)
to _address _entry.grid(column=2, row=5, stick=W)


#Labels
ttk.Label(mainframe, text="Login Email:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Login Password:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Message:").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Send Amount:").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Victim:").grid(column=1, row=5, sticky=W)


#Buttons
ttk.Button(mainframe,text="Start Spamming!", command=start_spam).grid(column=4, row=2, sticky=W)

from child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)
username_entry.focus()
root.mainloop()
        







