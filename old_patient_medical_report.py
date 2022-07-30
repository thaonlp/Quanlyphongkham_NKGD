from tkinter import *
import sqlite3
from datetime import datetime

from tkinter import messagebox

LEFTSIDE_START = 10
LABEL_LENGTH = 150

databaseFile = "hsbn.db"

'''TABLE PhieuKhamBenh
        (ID INT PRIMARY KEY     NOT NULL,
        PATIENTID INT NOT NULL,
        CHECKDAY CHAR(20),
        REASON CHAR(100),
        PLAN TEXT NOT NULL,
        FOREIGN KEY (PATIENTID) REFERENCES BenhNhan (ID));'''

class OldPatientMedicalReport(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.id = StringVar()
        self.patientId = StringVar()
        self.patientName = StringVar()
        self.phone = StringVar()
        self.address = StringVar()
        self.checkDay = StringVar()
        self.reason = StringVar()
        self.plan = None
        self.today = StringVar()

        self.sex_choice = IntVar()
        self.variable_text_map = {
            "Số phiếu khám bệnh": self.id,
            "Mã số bệnh nhân": self.patientId,
            "Ngày khám": self.checkDay,
            "Lý do tới khám": self.reason,
            "Kế hoạch điều trị": self.plan,
        }
        mainlbl=Label(self, text="Phiếu điều trị", fg='red', font=("Helvetica", 28, "bold italic"))
        mainlbl.place(x=LEFTSIDE_START + 300, y=5)
        #Button(self,
        #       text='Close',
        #       command=self.close_window).pack(expand=True)
        self.initUI()
        self.title('Nha khoa Gia Định - Phiếu khám bệnh')
        self.geometry("800x800+10+20")

    def initUI(self):
        self.create_window_label_with_entry("Số phiếu khám bệnh", LEFTSIDE_START, 50)
        self.create_window_label_with_entry("Mã số bệnh nhân", LEFTSIDE_START, 80)
        self.create_window_label_with_auto_entry("Ngày khám", self.today, LEFTSIDE_START, 170)
        self.create_window_label_with_entry("Lý do tới khám", LEFTSIDE_START, 200)
        self.create_text_box("Kế hoạch điều trị", LEFTSIDE_START, 230)
        # Button
        findBtn = Button(self, text="Tìm bệnh nhân", fg='green', font=("Times", 15, "bold italic"), command=self.search_for_patient)
        findBtn.place(x=400, y=80)
        dateBtn = Button(self, text="Ngày hôm nay", fg='green', font=("Times", 15, "bold italic"), command=self.insert_date_auto)
        dateBtn.place(x=400, y=170)
        saveBtn=Button(self, text="Lưu thông tin", fg='green', font=("Times", 15, "bold italic"), command=self.save_Data)
        saveBtn.place(x=LEFTSIDE_START + 330, y=750)
        exitBtn=Button(self, text="Thoát", fg='green', font=("Times", 15, "bold italic"), command=self.close_window)
        exitBtn.place(x=LEFTSIDE_START + 650, y=750)

    def create_window_label_with_entry(self, text, x, y):
        lbl=Label(self, text=text, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        txtfld=Entry(self, text=self.variable_text_map[text], bd=3)
        txtfld.place(x=x+LABEL_LENGTH,y=y)

    def create_window_label_with_auto_entry(self, text, var, x, y):
        lbl=Label(self, text=text, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        txtfld=Entry(self, text=self.variable_text_map[text], textvariable=var, bd=3)
        txtfld.place(x=x+LABEL_LENGTH,y=y)


    def create_text_box(self, label, x, y):
        lbl=Label(self, text=label, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        self.text_box = Text(self, bd=3, height = 10, width = 40, wrap='word')
        self.text_box.place(x=x+LABEL_LENGTH, y=y)

    def insert_date_auto(self):
        today = datetime.date(datetime.now())
        self.today.set(today)


    def search_for_patient(self):
        patientId = self.variable_text_map["Mã số bệnh nhân"].get()
        if patientId != "" :
            self.patientId = patientId
        else:
            messagebox.showerror("Tìm bệnh nhân", "Chưa nhập Mã số bệnh nhân")
        query = "SELECT FULLNAME,PHONE,ADDRESS FROM BenhNhan WHERE ID = '" + patientId.upper() + "';"
        print("Performing query: " , query)
        con = sqlite3.connect(databaseFile)
        cursorObj = con.cursor()
        cursorObj.execute(query)
        results = cursorObj.fetchall()
        print(results)
        nameText = StringVar()
        addressText = StringVar()
        fullname = Label(self, text="Tên bệnh nhân", fg='blue',font=("Times", 15)).place(x=LEFTSIDE_START, y = 110)
        nameBox = Entry(self, textvariable=nameText, width=40)
        nameText.set(results[0][0])
        nameBox.place(x=LEFTSIDE_START + LABEL_LENGTH, y=110)
        if results[0][1] != None:
            phoneText = StringVar()
            phone = Label(self, text="Số điện thoại", fg='blue',font=("Times", 15)).place(x=LEFTSIDE_START + 200, y = 110)
            phoneBox = Entry(self, textvariable=phoneText)
            phoneText.set(results[0][1])
            phoneBox.place(x=LEFTSIDE_START + 200 + LABEL_LENGTH, y = 110)
        address = Label(self, text="Địa chỉ", fg='blue',font=("Times", 15)).place(x=LEFTSIDE_START, y = 140)
        addressBox = Entry(self, textvariable=addressText, width=40)
        addressText.set(results[0][2])
        addressBox.place(x=LEFTSIDE_START + LABEL_LENGTH, y=140)
        con.close()


    def sql_insert_PhieuKhamBenh(self, con, entities):
        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO PhieuKhamBenh(ID,PATIENTID,CHECKDAY,REASON,PLAN) VALUES(?, ?, ?, ?, ?)', entities)
        con.commit()

    def save_Data(self):
        conn = sqlite3.connect(databaseFile)
        print("Opened database successfully")
        d = lambda: [self.variable_text_map[data].get() for data in self.variable_text_map]
        print(d())
        for data in self.variable_text_map:
            content = self.variable_text_map[data].get()
            print(content)

        self.sql_insert_PhieuKhamBenh(conn, content)
        for v in self.note:
            if not v.get()=="off":
                print(v.get())
        self.plan = self.text_box.get(1.0, END)

        print("Data saved!")
        messagebox.showinfo("Tạo phiếu khám bệnh mới", "Đã lưu thông tin")

        conn.commit()
        conn.close()

    def close_window(self):
        self.destroy()

