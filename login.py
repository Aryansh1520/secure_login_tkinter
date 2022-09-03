import cx_Oracle
from tkinter import *
import time

root = Tk()
root.geometry('400x300')

dsn_tns = cx_Oracle.makedsn('aryan-virtual-machine', '1521', service_name='XE')
conn = cx_Oracle.connect(user=r'aryan_user', password='1520', dsn=dsn_tns)
c = conn.cursor()

class page2:
    def __init__(self,root) :
        for widgets in root.winfo_children():
            print(widgets)
            widgets.forget()


def cursor_on():
    global c , conn
    conn = cx_Oracle.connect(user=r'aryan_user', password='1520', dsn=dsn_tns)
    c = conn.cursor()

def verify_admin_login(root):
    cursor_on()
    usrn , passwrd = username_label.get(),password_label.get()
    x = c.execute('SELECT password FROM admin WHERE name = :var',var = usrn)
    for password in x:
        if password[0]==passwrd:
            print("LOGIN SUCCESSFUL")
            print("LOGIN SUCCESSFUL ...redirecting to dashboard in 3,2,1")
            time.sleep(3)
            page2(root)
        else :
            print("USERNAME AND/OR PASSWORD IS/ARE WRONG")
    conn.close()

username_label = Entry(root,width=20)
password_label = Entry(root,width=20,show='*')
admin_log_lab = Label(root,text='admin login')
admin_log_butt = Button(root,text='log-in',command  = lambda  :verify_admin_login(root))

admin_log_lab.pack()
username_label.pack()
password_label.pack()
admin_log_butt.pack()


root.mainloop()
