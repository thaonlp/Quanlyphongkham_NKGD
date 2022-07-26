from tkinter import *
import sqlite3

LEFTSIDE_START = 10
LABEL_LENGTH = 150

tienSuBenh = ["Không có", "Tiểu đường", "Tim mạch", "Thận, gan, bao tử", "Lao", "Suyễn", "Máu không đông"]

databaseFile = "hsbn.db"

class MedicalReport(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.id = StringVar()
        self.name = StringVar()
        self.sex = StringVar()
        self.job = StringVar()
        self.birth = IntVar()
        self.phone = StringVar()
        self.checkDay = StringVar()
        self.address = StringVar()
        self.reason = StringVar()
        self.history = StringVar()
        self.otherHistory = StringVar()
        self.allergy = StringVar()
        self.plan = StringVar()
        self.variable_text_map = {
            "Số hồ sơ": self.id,
            "Họ tên": self.name,
            "Giới tính": self.sex,
            "Năm sinh": self.birth,
            "Nghề nghiệp": self.job,
            "Số điện thoại": self.phone,
            "Ngày khám": self.checkDay,
            "Địa chỉ": self.address,
            "Lý do tới khám": self.reason,
            "Tiền sử bệnh": self.history,
            "Tiền sử bệnh khác": self.otherHistory,
            "Tiền sử dị ứng": self.allergy,
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
        self.create_window_label_with_entry("Số hồ sơ", LEFTSIDE_START, 50)
        self.create_window_label_with_entry("Họ tên", LEFTSIDE_START, 80)
        self.create_true_false_text_box_with_label("Giới tính", "Nam", "Nữ", LEFTSIDE_START, 110)
        self.create_window_label_with_entry_2nd_colum("Năm sinh", LEFTSIDE_START, 110)
        self.create_window_label_with_entry("Nghề nghiệp", LEFTSIDE_START, 140)
        self.create_window_label_with_entry_2nd_colum("Số điện thoại", LEFTSIDE_START, 140)
        self.create_window_label_with_entry("Ngày khám", LEFTSIDE_START, 170)
        self.create_window_label_with_entry("Địa chỉ", LEFTSIDE_START, 200)
        self.create_window_label_with_entry("Lý do tới khám", LEFTSIDE_START, 230)
        self.create_multiple_choices_with_label("Tiền sử bệnh", tienSuBenh, LEFTSIDE_START, 260)
        self.create_window_label_with_entry("Tiền sử bệnh khác", LEFTSIDE_START, 470)
        self.create_window_label_with_entry("Tiền sử dị ứng", LEFTSIDE_START, 500)
        self.create_text_box("Kế hoạch điều trị", LEFTSIDE_START, 530)
        # Button
        saveBtn=Button(self, text="Lưu thông tin", fg='green', font=("Times", 15, "bold italic"), command=self.save_Data)
        saveBtn.place(x=LEFTSIDE_START + 330, y=750)
        exitBtn=Button(self, text="Thoát", fg='green', font=("Times", 15, "bold italic"), command=self.close_window)
        exitBtn.place(x=LEFTSIDE_START + 650, y=750)

    def create_window_label_with_entry(self, text, x, y):
        lbl=Label(self, text=text, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        txtfld=Entry(self, text=self.variable_text_map[text], bd=3)
        txtfld.place(x=x+LABEL_LENGTH,y=y)

    def create_window_label_with_entry_2nd_colum(self,text, x, y):
        lbl=Label(self, text=text, fg='blue', font=("Times", 15))
        lbl.place(x=x+400, y=y)
        txtfld=Entry(self, text=self.variable_text_map[text], bd=3)
        txtfld.place(x=x+400+LABEL_LENGTH,y=y)

    def create_true_false_text_box_with_label(self,label,c1, c2, x,y):
        lbl=Label(self, text=label, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        v0=IntVar()
        v0.set(1)
        r1=Radiobutton(self, text=c1, variable=v0,value=1)
        r2=Radiobutton(self, text=c2, variable=v0,value=2)
        r1.place(x=x + LABEL_LENGTH ,y=y)
        r2.place(x=x + LABEL_LENGTH + 60, y=y)

    def create_choice(self,label,x,y):
        choice = Checkbutton(self, text=label, variable = label)
        choice.place(x=x, y = y)

    def create_multiple_choices_with_label(self, mainLable, list_of_choices, x, y):
        lbl=Label(self, text=mainLable, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        for c in range(len(list_of_choices)):
            self.create_choice(list_of_choices[c], x=x+LABEL_LENGTH, y = y + 30 * c)

    def create_text_box(self, label, x, y):
        lbl=Label(self, text=label, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        self.text_box = Text(self, bd=3, height = 10, width = 40, wrap='word')
        self.text_box.place(x=x+LABEL_LENGTH, y=y)

    def open_data(self):
       text_file = open(databaseFile, "r")
       content = text_file.read()
       self.text_box.insert(END, content)
       text_file.close()

    def sql_insert_BenhNhan(self, con, entities):
        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO BenhNhan(PATIENTID,NAME,SEX,DOB,JOB,PHONE,ADDRESS,REASON,HISTORY,OTHERHIST,ALLERGY) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
        con.commit()

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
        self.text_box.get(1.0, END)
        self.sql_insert(conn, d())
        print("Data saved!")
        conn.close()

    def close_window(self):
        self.destroy()

