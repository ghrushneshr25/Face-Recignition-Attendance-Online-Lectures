from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        # =====Login Frame============
        self.Frame_login = Frame(self.root, bg="white")
        self.Frame_login.place(x=125, y=200, height=340, width=400)

        title = Label(self.Frame_login, text="Login Here", font=(
            "Impact", 35, "bold"), fg="#5465ff", bg="white")
        title.place(x=25, y=30)

        desc = Label(self.Frame_login, text="Student Login", font=(
            "Goudy old style", 15, "bold"), fg="#788bff", bg="white")
        desc.place(x=25, y=100)

        label_user = Label(self.Frame_login, text="Username", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        label_user.place(x=25, y=140)

        self.txt_user = Entry(self.Frame_login, font=(
            "times new roman", 15), bg="lightgray")

        self.txt_user.place(x=25, y=170, width=350, height=35)

        label_pass = Label(self.Frame_login, text="Password", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        label_pass.place(x=25, y=210)

        self.txt_pass = Entry(self.Frame_login, font=(
            "times new roman", 15), bg="lightgray", show='*')

        self.txt_pass.place(x=25, y=240, width=350, height=35)

        self.login_btn = Button(self.root, text="Login", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.login)

        self.login_btn.place(x=180, y=525)

        self.register_btn = Button(self.root, text="Register", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.registerButton)

        self.register_btn.place(x=330, y=525)

    def checkCredentials(self, rollno, passcode):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="abcd1234",
                database="attendance"
            )
            cursor = mydb.cursor()
            sqlQuery = "SELECT PASSWORD FROM STUDENTDETAILS WHERE ROLLNO = '"+rollno+"'"
            cursor.execute(sqlQuery)
            record = cursor.fetchone()
            if (record[0] == passcode):
                return True
            else:
                return False
        except Exception as e:
            return False
        return False

    def login(self):

        username = self.txt_user.get()
        password = self.txt_pass.get()

        if username != "" and password != "":

            logIn = self.checkCredentials(username, password)
            if(logIn == True):
                self.Frame_login.destroy()
                self.login_btn.destroy()
                self.register_btn.destroy()
                loggedin = Loggedin(root)
            else:
                messagebox.showerror(
                    "Error", "Invalid Credentials", parent=self.root)

        else:
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)

    def registerButton(self):
        self.Frame_login.destroy()
        self.register_btn.destroy()
        self.login_btn.destroy()
        registerHere = Register(root)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")

        self.backButton = Button(self.root, text="Back", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.backpress)
        self.backButton.place(x=0, y=0)

        # --- REGISTER FRAME----
        self.Frame_register = Frame(self.root, bg="white")
        self.Frame_register.place(x=225, y=25, height=740, width=400)

        title = Label(self.Frame_register, text="Register", font=(
            "Impact", 35, "bold"), fg="#5465ff", bg="white")
        title.place(x=20, y=30)

        desc = Label(self.Frame_register, text="Student Register", font=(
            "Goudy old style", 15, "bold"), fg="#788bff", bg="white")
        desc.place(x=20, y=100)

        labelRollNo = Label(self.Frame_register, text="Roll No", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelRollNo.place(x=20, y=140)

        self.txtRollNo = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtRollNo.place(x=20, y=170, width=160, height=35)

        labelDiv = Label(self.Frame_register, text="Div", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelDiv.place(x=220, y=140)

        self.txtDiv = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtDiv.place(x=220, y=170, width=160, height=35)

        labelName = Label(self.Frame_register, text="Name", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelName.place(x=20, y=210)

        self.txtName = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtName.place(x=20, y=240, width=360, height=35)

        labelEmailId = Label(self.Frame_register, text="Email ID", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelEmailId.place(x=20, y=280)

        self.txtEmailId = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray")

        self.txtEmailId.place(x=20, y=310, width=360, height=35)

        "-------------------------------------------------------"

        labelYear = Label(self.Frame_register, text="Year", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelYear.place(x=20, y=350)

        self.currentYear = StringVar(None)
        self.currentYear.set("FE")

        self.radioYearFE = Radiobutton(self.Frame_register, text="FE", variable=self.currentYear, value="FE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearFE.place(x=20, y=380, width=90, height=35)

        self.radioYearSE = Radiobutton(self.Frame_register, text="SE", variable=self.currentYear, value="SE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearSE.place(x=110, y=380, width=90, height=35)

        self.radioYearTE = Radiobutton(self.Frame_register, text="TE", variable=self.currentYear, value="TE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearTE.place(x=200, y=380, width=90, height=35)

        self.radioYearBE = Radiobutton(self.Frame_register, text="BE", variable=self.currentYear, value="BE", font=(
            "times new roman", 15), bg="lightgray")

        self.radioYearBE.place(x=290, y=380, width=90, height=35)

        "------------------------------------------------------"

        labelBranch = Label(self.Frame_register, text="Branch", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelBranch.place(x=20, y=420)

        self.selectedBranch = StringVar()
        self.selectedBranch.set("COMPUTER ENGINEERING")

        self.radioBranchCOMPS = Radiobutton(self.Frame_register, text="Computer", variable=self.selectedBranch, value="COMPUTER ENGINEERING", font=(
            "times new roman", 15), bg="lightgray", justify=LEFT)
        self.radioBranchCOMPS.place(x=20, y=450, width=360, height=35)

        self.radioBranchIT = Radiobutton(self.Frame_register, text="Information Technology", variable=self.selectedBranch, value="INFORMATION TECHNOLOGY", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchIT.place(x=20, y=480, width=360, height=35)

        self.radioBranchEXTC = Radiobutton(self.Frame_register, text="Electronics and Telecommunication", variable=self.selectedBranch, value="ELECTRONICS AND TELECOMMUNICATION ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchEXTC.place(x=20, y=510, width=360, height=35)

        self.radioBranchETRX = Radiobutton(self.Frame_register, text="Electronics", variable=self.selectedBranch, value="ELECTRONICS ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchETRX.place(x=20, y=540, width=360, height=35)

        self.radioBranchINSTRU = Radiobutton(self.Frame_register, text="Instrumentation", variable=self.selectedBranch, value="INSTRUMENTATION ENGINEERING", font=(
            "times new roman", 15), bg="lightgray",  justify=LEFT)
        self.radioBranchINSTRU.place(x=20, y=570, width=360, height=35)

        "--------------------------------------------------------"
        labelPassword = Label(self.Frame_register, text="Password", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="white")
        labelPassword.place(x=20, y=610)

        self.txtPassword = Entry(self.Frame_register, font=(
            "times new roman", 15), bg="lightgray", show='*')

        self.txtPassword.place(x=20, y=640, width=360, height=35)

        self.registerButton = Button(self.Frame_register, text="Register", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.registerNow)
        self.registerButton.place(x=250, y=690)

    def registerNow(self):

        rollNo = self.txtRollNo.get()
        div = self.txtDiv.get()
        name = self.txtName.get()
        email = self.txtEmailId.get()
        year = self.currentYear.get()
        branch = self.selectedBranch.get()
        password = self.txtPassword.get()

        if rollNo == "" or div == "" or name == "" or email == "" or branch == "" or password == "" or year == "":
            messagebox.showerror(
                "Error", "Invalid Credentials", parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="abcd1234",
                    database="attendance"
                )
                cursor = mydb.cursor()
                query = "INSERT INTO studentdetails (`RollNo`, `name`, `email id`, `year` , `branch`, `password`, `div`) VALUES ( %s, %s , %s, %s, %s , %s, %s)"
                record = (rollNo, name, email, year, branch, password, div)
                # print(query, record)
                cursor.execute(query, record)
                mydb.commit()
                messagebox.showinfo(message="Successful registration!")
                self.backpress()
            except mysql.connector.Error as e:
                if e.errorcode == 1062:
                    messagebox.showerror(message="User already registered")
                else:
                    messagebox.showerror(message="Error")
                self.backpress()
                mydb.rollback()
            finally:
                if mydb is not None:
                    cursor.close()
                    mydb.close()

    def backpress(self):
        self.Frame_register.destroy()
        self.backButton.destroy()
        logindisplay = Login(root)


class Loggedin:
    def __init__(self, root):
        self.root = root
        self.root.title("Logged In")
        self.backButton = Button(self.root, text="Back", bg="#d77337", fg="white", font=(
            "times new roman", 15), width=10, command=self.backpress)
        self.backButton.place(x=0, y=0)

    def backpress(self):
        self.backButton.destroy()
        logindisplay = Login(root)


root = Tk()
width = 1280
height = 800
root.geometry("%dx%d" % (width, height))
bg = PhotoImage(file="studentattendance.png")
bg_image = Label(root, image=bg).place(
    x=0, y=0, relwidth=1, relheight=1)
root.resizable(False, False)
login = Login(root)
root.mainloop()
