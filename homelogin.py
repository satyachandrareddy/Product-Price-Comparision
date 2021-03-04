import sqlite3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Product Price Comparision Software")
root.configure(background='orange')

# ---Variables---
UserName = StringVar()
Password = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
CF = StringVar()
SpecialSym = ['$', '@', '#', '%']


# ---Methods---
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_satya.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `satya` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, "
        "password TEXT, firstname TEXT, lastname TEXT,cf TEXT)")


def home():
    global c
    c = Frame(root)
    c.pack()
    root.configure(background='skyblue')
    c.configure(background='skyblue')
    labTitle = Label(c, text="HOME", font=('courier', 45, 'bold'), fg='black', bg='skyblue', bd=20)
    labTitle.grid(row=0, column=0, columnspan=2, pady=20)
    # c1 = Frame(c, width=800, height=400, bd=10, relief='flat')
    # c1.grid(row=1, column=0)
    btn = Button(c, text="Main", width=13, bg='pink', font=('arial', 20, 'bold'), command=imp)
    btn.grid(row=2, column=1)
    btn = Button(c, text="Sign Out", width=13, bg='pink', font=('arial', 20, 'bold'), command=logout)
    btn.grid(row=3, column=1)


def imp():
    root.destroy()
    import main


def logout():
    result = messagebox.askquestion('Price Comparision', 'Are you sure you want to log out?', icon="warning")
    if result == 'yes':
        c.destroy()
        LoginForm()
    erase()


def back():
    menubar.destroy()
    RegisterFrame.destroy()
    LoginForm()
    erase()


def erase():
    UserName.set("")
    Password.set("")


def Reset():
    UserName.set("")
    Password.set("")
    FIRSTNAME.set('')
    LASTNAME.set('')
    CF.set('')


def LoginForm():
    global LoginFrame
    LoginFrame = Frame(root)
    LoginFrame.pack()
    LoginFrame.configure(background='pink')
    LabelTitle = Label(LoginFrame, text="PRODUCT PRICE COMPARISION", font=('arial', 50, 'bold'), fg='red', bg='pink',
                       bd=20)
    LabelTitle.grid(row=0, column=0, columnspan=3, pady=20)

    Loginframe1 = Frame(LoginFrame, width=800, height=300, bd=20, relief='flat', bg='pink')
    Loginframe1.grid(row=1, column=0, columnspan=3)
    Loginframe2 = Frame(LoginFrame, width=800, height=100, bd=20, relief='flat', bg='pink')
    Loginframe2.grid(row=2, column=0, columnspan=3)
    Loginframe3 = Frame(LoginFrame, width=800, height=200, bd=20, relief='flat', bg='pink')
    Loginframe3.grid(row=3, column=0, pady=2, columnspan=3)
    lbl_username = Label(Loginframe1, text="Username:", font=('arial', 25), bd=18, bg='pink')
    lbl_username.grid(row=1, pady=2)
    lbl_password = Label(Loginframe1, text="Password:", font=('arial', 25), bd=18, bg='pink')
    lbl_password.grid(row=2, pady=2)

    username = Entry(Loginframe1, font=('arial', 20), textvariable=UserName, width=15)
    username.grid(row=1, column=1)
    password = Entry(Loginframe1, font=('arial', 20), textvariable=Password, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(Loginframe2, text="Login", font=('arial', 20, 'bold'), fg='green', width=12, command=Login)
    btn_login.grid(row=0, column=0)
    btnReset = Button(Loginframe2, text="Reset", width=13, font=('arial', 20, 'bold'), fg='red', command=erase)
    btnReset.grid(row=0, column=1)
    btnReg = Button(Loginframe3, text="Register", width=13, font=('arial', 20, 'bold'), fg='purple', command=ToggleToRegister)
    btnReg.grid(row=0, column=1)


def RegisterForm():
    global RegisterFrame, menubar
    RegisterFrame = Frame(root)
    RegisterFrame.pack()
    RegisterFrame.configure(background='orange')
    menubar = Menu(root)
    menubar.add_cascade(label="<- Back", command=back)
    root.config(menu=menubar)
    labTitle = Label(RegisterFrame, text="Sign Up", font=('arial', 50, 'bold'), fg='red', bd=20, bg='orange')
    labTitle.grid(row=0, column=0, columnspan=2, pady=20)

    Regframe1 = Frame(RegisterFrame, width=800, height=400, bd=20, bg='orange', relief='flat')
    Regframe1.grid(row=1, column=1)
    Regframe2 = Frame(RegisterFrame, width=800, height=100, bd=20, bg='orange', relief='flat')
    Regframe2.grid(row=2, column=1)

    lbl_username = Label(Regframe1, text="Username:", font=('arial', 18), bd=18, bg='orange')
    lbl_username.grid(row=3)
    lbl_password = Label(Regframe1, text="Password:", font=('arial', 18), bd=18, bg='orange')
    lbl_password.grid(row=4)
    lbl_firstname = Label(Regframe1, text="Confirm Password:", font=('arial', 18), bd=18, bg='orange')
    lbl_firstname.grid(row=5)
    lbl_firstname = Label(Regframe1, text="First Name:", font=('arial', 18), bd=18, bg='orange')
    lbl_firstname.grid(row=1)
    lbl_lastname = Label(Regframe1, text="Last Name:", font=('arial', 18), bd=18, bg='orange')
    lbl_lastname.grid(row=2)

    username = Entry(Regframe1, font=('arial', 20), textvariable=UserName, width=15)
    username.grid(row=3, column=1)
    password = Entry(Regframe1, font=('arial', 20), textvariable=Password, width=15, show="*")
    password.grid(row=4, column=1)
    cf = Entry(Regframe1, font=('arial', 20), textvariable=CF, width=15, show="*")
    cf.grid(row=5, column=1)
    firstname = Entry(Regframe1, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=1, column=1)
    lastname = Entry(Regframe1, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=2, column=1)
    btn_login = Button(Regframe2, text="Register", font=('arial', 20, 'bold'), fg='limegreen', width=13,
                       command=Register)
    btn_login.grid(row=0, column=0, pady=20)
    bttnReset = Button(Regframe2, text="Reset", width=13, font=('arial', 20, 'bold'), fg='red', command=Reset)
    bttnReset.grid(row=0, column=1)


def ToggleToLogin(event=None):
    menubar.destroy()
    RegisterFrame.destroy()
    LoginForm()


def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()


def Register():
    Database()
    if UserName.get() == "" or Password.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get() == "" or CF.get() == '':
        messagebox.showinfo("Price Comparision", "Please fill the following fields")
    else:
        cursor.execute("SELECT * FROM `satya` WHERE `username` = ?", (UserName.get(),))
        if cursor.fetchone() is not None:
            messagebox.showinfo("Price Comparision", "User Name is already taken")
        else:
            if len(UserName.get()) >= 6 and len(Password.get()) >= 6 and any(
                    char.isdigit() for char in Password.get()) and any(
                char.isupper() for char in Password.get()) and any(char in SpecialSym for char in Password.get()):
                if Password.get() == CF.get():

                    cursor.execute(
                        "INSERT INTO `satya` (username, password, firstname, lastname, cf) VALUES(?, ?, ?, ?, ?)",
                        (str(UserName.get()), str(Password.get()), str(FIRSTNAME.get()), str(LASTNAME.get()), CF.get()))
                    conn.commit()
                    answer = messagebox.showinfo("Price Comparision", "Account successfully created")
                    if (answer == 'ok'):
                        UserName.set("")
                        Password.set("")
                        FIRSTNAME.set("")
                        LASTNAME.set("")
                        CF.set("")
                        ToggleToLogin()
                else:
                    messagebox.showinfo("Price Comparision", "Password and Confirm Password should be same")
            else:
                messagebox.showinfo("Price Comparision",
                                    "User Name and Password should contains at least 6 characters and Password should "
                                    "contain a numerical, an uppercase letter, a lowercase letter and a special symbol "
                                    "among @,$,% and %.")
        cursor.close()
        conn.close()


def Login():
    Database()
    if UserName.get() == "" or Password.get() == "":
        messagebox.showerror("Price Comparision", "Please complete the following fields")
    else:
        cursor.execute("SELECT * FROM `satya` WHERE `username` = ? and `password` = ?",
                       (UserName.get(), Password.get()))
        if cursor.fetchone() is not None:
            messagebox.showinfo("Price Comparision", "Account successfully logged in")
            LoginFrame.destroy()
            home()
        else:
            messagebox.showinfo("Price Comparision", "Invalid User Name or Password")


LoginForm()

# ---Initialization---
if __name__ == '__main__':
    root.minsize(600, 600)
    root.mainloop()
