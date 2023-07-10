from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management Sysytem")
        self.root.geometry("930x620+0+0")

        # variable
        self.member_var = StringVar()
        self.Id_var = StringVar()
        self.usn = StringVar()
        self.fn_var = StringVar()
        self.ln_var = StringVar()
        self.pno_var = StringVar()
        self.bid_var = StringVar()
        self.bn_var = StringVar()
        self.an_var = StringVar()
        self.db_var = StringVar()
        self.dd_var = StringVar()
        self.days_var = StringVar()
        self.fine_var = StringVar()
        self.total_var = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg='orange', bd=17,
                         relief=RIDGE,
                         font=('times new roman', 30, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=100, width=950, height=300)

        # DataFrameLeft

        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg='orange', bd=8,
                                   relief=RIDGE,
                                   font=('times new roman', 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=540, height=250)

        lbl_Member = Label(DataFrameLeft, bg="powderblue", text=
        "Member Type", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lbl_Member.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var, font=("times new roman", 10, "bold"),
                                 width=19, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Faculty")
        comMember.grid(row=0, column=1)

        lblId = Label(DataFrameLeft, bg="powderblue", text=
        "Id", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblId.grid(row=1, column=0, sticky=W)

        txtsid = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.Id_var, width=22)
        txtsid.grid(row=1, column=1)

        lblUSN = Label(DataFrameLeft, bg="powderblue", text=
        "USN", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblUSN.grid(row=2, column=0, sticky=W)

        txtusn = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.usn, width=22)
        txtusn.grid(row=2, column=1)

        lblFN = Label(DataFrameLeft, bg="powderblue", text=
        "First Name", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblFN.grid(row=3, column=0, sticky=W)

        txtfn = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.fn_var, width=22)
        txtfn.grid(row=3, column=1)

        lblLN = Label(DataFrameLeft, bg="powderblue", text=
        "Last Name", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblLN.grid(row=4, column=0, sticky=W)

        txtln = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.ln_var, width=22)
        txtln.grid(row=4, column=1)

        lblmobile = Label(DataFrameLeft, bg="powderblue", text=
        "Phone no.", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky=W)

        txtmobile = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.pno_var, width=22)
        txtmobile.grid(row=5, column=1)

        lblbookid = Label(DataFrameLeft, bg="powderblue", text=
        "Book Id", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblbookid.grid(row=6, column=0, sticky=W)

        txtbid = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.bid_var, width=22)
        txtbid.grid(row=6, column=1)

        lblbookname = Label(DataFrameLeft, bg="powderblue", text=
        "Book Title", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblbookname.grid(row=0, column=2, sticky=W)

        txtbn = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.bn_var, width=22)
        txtbn.grid(row=0, column=3)

        lblauthor = Label(DataFrameLeft, bg="powderblue", text=
        "Author name", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblauthor.grid(row=1, column=2, sticky=W)

        txtan = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.an_var, width=22)
        txtan.grid(row=1, column=3)

        lblDateB = Label(DataFrameLeft, bg="powderblue", text=
        "Date Borrowed", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblDateB.grid(row=2, column=2, sticky=W)

        txtdb = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.db_var, width=22)
        txtdb.grid(row=2, column=3)

        lblDatedue = Label(DataFrameLeft, bg="powderblue", text=
        "Date Due", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblDatedue.grid(row=3, column=2, sticky=W)

        txtdd = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.dd_var, width=22)
        txtdd.grid(row=3, column=3)

        lblnd = Label(DataFrameLeft, bg="powderblue", text=
        "Days over due", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblnd.grid(row=4, column=2, sticky=W)

        txtnd = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.days_var, width=22)
        txtnd.grid(row=4, column=3)

        lblfine = Label(DataFrameLeft, bg="powderblue", text=
        "Fine", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblfine.grid(row=5, column=2, sticky=W)

        txtfine = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.fine_var, width=22)
        txtfine.grid(row=5, column=3)

        lblTB = Label(DataFrameLeft, bg="powderblue", text=
        "Total books", font=("times new roman", 10, "bold"), padx=2, pady=6)
        lblTB.grid(row=6, column=2, sticky=W)

        txtTB = Entry(DataFrameLeft, font=("times new roman", 10, "bold"), textvariable=self.total_var, width=22)
        txtTB.grid(row=6, column=3)

        # DataFrameRight

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg='orange', bd=12,
                                    relief=RIDGE,
                                    font=('times new roman', 12, "bold"))
        DataFrameRight.place(x=540, y=5, width=350, height=250)

        self.txtBox = Text(DataFrameRight, font=('times new roman', 10, "bold"), width=23, height=13, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = ['B.S. Grewal', 'Glyn James', 'Data Structures', 'Digital Electronis', 'Java ','Data base System','Python Programming']

        def SelectBook(event):
            value = str(listBox.get(listBox.curselection()))

            if value == "B.S. Grewal":
                self.bid_var.set("Bid5")
                self.bn_var.set("Higher Engineering Mathematics")
                self.an_var.set(" Khanna Publishers")
                d1 = datetime.datetime.today().date()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.db_var.set(d1)
                self.dd_var.set(d2)
                self.days_var.set(d3)
                self.fine_var.set("20")
                self.total_var.set("50")
            elif(value == "Glyn James"):
                self.bid_var.set("Bid4")
                self.bn_var.set("Advanced Modern Engineering Mathematics")
                self.an_var.set("Pearson Education")
                d1 = datetime.datetime.today().date()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.db_var.set(d1)
                self.dd_var.set(d2)
                self.days_var.set(d3)
                self.fine_var.set("30")
                self.total_var.set("10")
            elif (value == "Data Structures"):
                self.bid_var.set("Bid6")
                self.bn_var.set("A Pseudocode Approach")
                self.an_var.set("Richard.F.Gilberg")
                d1 = datetime.datetime.today().date()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.db_var.set(d1)
                self.dd_var.set(d2)
                self.days_var.set(d3)
                self.fine_var.set("40")
                self.total_var.set("38")
            elif (value == "Digital Electronis"):
                self.bid_var.set("Bid9")
                self.bn_var.set("Digital Principles and Applications")
                self.an_var.set("Donald P Leach")
                d1 = datetime.datetime.today().date()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.db_var.set(d1)
                self.dd_var.set(d2)
                self.days_var.set(d3)
                self.fine_var.set("26")
                self.total_var.set("60")
            elif (value == "Java"):
                self.bid_var.set("Bid3")
                self.bn_var.set("Java Fundamentals")
                self.an_var.set("Herbert Schildt")
                d1 = datetime.datetime.today().date()
                temp = datetime.timedelta(days=15)
                d2=temp.date()
                d3 = d1 + d2
                self.db_var.set(d1)
                self.dd_var.set(d2)
                self.days_var.set(d3)
                self.fine_var.set("25")
                self.total_var.set("44")
            elif (value == "Data base System"):
                self.bid_var.set("Bid15")
                self.bn_var.set("Data base System Concepts")
                self.an_var.set("Silberschatz")
                d1 = datetime.datetime.today().date()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.db_var.set(d1)
                self.dd_var.set(d2)
                self.days_var.set(d3)
                self.fine_var.set("18")
                self.total_var.set("3")
            elif (value == "Python Programming"):
                self.bid_var.set("Bid1")
                self.bn_var.set("Python Programming, Shroff/Murach")
                self.an_var.set("Michael Urban")
                d1 = datetime.datetime.today().date()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.db_var.set(d1)
                self.dd_var.set(d2)
                self.days_var.set(d3)
                self.fine_var.set("40")
                self.total_var.set("5")


        listBox = Listbox(DataFrameRight, font=('times new roman', 10, "bold"), width=17, height=13)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # Buttons Frame Frame

        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=400, width=930, height=60)

        btnadd = Button(Framebutton, command=self.add_data, text="Add data", font=('times new roman', 11, "bold"),
                        width=15, bg="orange", fg="white")
        btnadd.grid(row=0, column=0)

        btnshow = Button(Framebutton, command=self.showData, text="Show data", font=('times new roman', 11, "bold"), width=15, bg="orange",
                         fg="white")
        btnshow.grid(row=0, column=1)

        btnupdate = Button(Framebutton,command=self.update, text="Update", font=('times new roman', 11, "bold"), width=15, bg="orange",
                           fg="white")
        btnupdate.grid(row=0, column=2)

        btndel = Button(Framebutton,command=self.delete, text="Delete", font=('times new roman', 11, "bold"), width=15, bg="orange",
                        fg="white")
        btndel.grid(row=0, column=3)

        btnreset = Button(Framebutton,command=self.reset, text="Reset", font=('times new roman', 11, "bold"), width=15, bg="orange",
                          fg="white")
        btnreset.grid(row=0, column=4)

        btnexit = Button(Framebutton,command=self.iExit, text="Exit", font=('times new roman', 11, "bold"), width=15, bg="orange",
                         fg="white")
        btnexit.grid(row=0, column=5)

        # Information Frame

        Framedetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framedetails.place(x=0, y=470, width=930, height=150)

        Table_frame = Frame(Framedetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=880, height=125)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column=(
            "Membertype", "Id", "Usn", "Firstname", "Lastname", "Phoneno.", "Bookid", "booktitle", "authorname",
            "Dateborrowed", "Datedue", "daysoverdue", "Fine", "totalbooks"), xscrollcommand=xscroll.set,
                                          yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview())
        yscroll.config(command=self.library_table.yview())

        self.library_table.heading("Membertype", text="Member Type")
        self.library_table.heading("Id", text="Id")
        self.library_table.heading("Usn", text="USN")
        self.library_table.heading("Firstname", text="First Name")
        self.library_table.heading("Lastname", text="Last Name")
        self.library_table.heading("Phoneno.", text="Phone no.")
        self.library_table.heading("Bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("authorname", text="Author Name")
        self.library_table.heading("Dateborrowed", text="Date Borrowed")
        self.library_table.heading("Datedue", text="Date due")
        self.library_table.heading("daysoverdue", text="Days over due")
        self.library_table.heading("Fine", text="Fine")
        self.library_table.heading("totalbooks", text="Total books")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Membertype", width=100)
        self.library_table.column("Id", width=100)
        self.library_table.column("Usn", width=100)
        self.library_table.column("Firstname", width=100)
        self.library_table.column("Lastname", width=100)
        self.library_table.column("Phoneno.", width=100)
        self.library_table.column("Bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("authorname", width=100)
        self.library_table.column("Dateborrowed", width=100)
        self.library_table.column("Datedue", width=100)
        self.library_table.column("daysoverdue", width=100)
        self.library_table.column("Fine", width=100)
        self.library_table.column("totalbooks", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="#root0110", database="lms")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.Id_var.get(),
            self.usn.get(),
            self.fn_var.get(),
            self.ln_var.get(),
            self.pno_var.get(),
            self.bid_var.get(),
            self.bn_var.get(),
            self.an_var.get(),
            self.db_var.get(),
            self.dd_var.get(),
            self.days_var.get(),
            self.fine_var.get(),
            self.total_var.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="#root0110", database="lms")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s,Id=%s,Firstname=%s,Lastname=%s,phone=%s,bookid=%s,booktitle=%s,author=%s,dateborrowed=%s,datedue=%s,days_over_due=%s,fine=%s,totalbooks=%s where usn=%s",(
            self.member_var.get(),
            self.Id_var.get(),
            self.fn_var.get(),
            self.ln_var.get(),
            self.pno_var.get(),
            self.bid_var.get(),
            self.bn_var.get(),
            self.an_var.get(),
            self.db_var.get(),
            self.dd_var.get(),
            self.days_var.get(),
            self.fine_var.get(),
            self.total_var.get(),
            self.usn.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="#root0110", database="lms")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in data:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.Id_var.set(row[1])
        self.usn.set(row[2])
        self.fn_var.set(row[3])
        self.ln_var.set(row[4])
        self.pno_var.set(row[13])
        self.bid_var.set(row[5])
        self.bn_var.set(row[6])
        self.an_var.set(row[7])
        self.db_var.set(row[8])
        self.dd_var.set(row[9])
        self.days_var.set(row[10])
        self.fine_var.set(row[11])
        self.total_var.set(row[12])
    def showData(self):
        self.txtBox.insert(END,"Member Type:"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "Id:" + self.Id_var.get() + "\n")
        self.txtBox.insert(END, "USN:" + self.usn.get() + "\n")
        self.txtBox.insert(END, "First Name:" + self.fn_var.get() + "\n")
        self.txtBox.insert(END, "Last Name:" + self.ln_var.get() + "\n")
        self.txtBox.insert(END, "Phone no.:" + self.pno_var.get() + "\n")
        self.txtBox.insert(END, "Book Id:" + self.bid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:" + self.bn_var.get() + "\n")
        self.txtBox.insert(END, "Author:" + self.an_var.get() + "\n")
        self.txtBox.insert(END, "Date borrowed:" + self.db_var.get() + "\n")
        self.txtBox.insert(END, "Date due:" + self.dd_var.get() + "\n")
        self.txtBox.insert(END, "days over due:" + self.days_var.get() + "\n")
        self.txtBox.insert(END, "Fine:" + self.fine_var.get() + "\n")
        self.txtBox.insert(END, "Total books:" + self.total_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.Id_var.set(""),
        self.usn.set(""),
        self.fn_var.set(""),
        self.ln_var.set(""),
        self.pno_var.set(""),
        self.bid_var.set(""),
        self.bn_var.set(""),
        self.an_var.set(""),
        self.db_var.set(""),
        self.dd_var.set(""),
        self.days_var.set(""),
        self.fine_var.set(""),
        self.total_var.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.usn.get()=="" or self.Id_var.get()=="":
            messagebox.showerror("Error","Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="#root0110", database="lms")
            my_cursor = conn.cursor()
            query="delete from library where usn=%s"
            value=(self.usn.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
