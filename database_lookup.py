import sqlite3
from tkinter import *

# add widgets here
LEFTSIDE_START = 10
LABEL_LENGTH = 150

databaseFile = "hsbn.db"

class PatientLookUp(Toplevel):
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

        mainlbl=Label(self, text="Thông tin bệnh nhân", fg='red', font=("Helvetica", 28, "bold italic"))
        mainlbl.place(x=LEFTSIDE_START + 300, y=5)

        self.initUI()
        self.title('Nha khoa Gia Định - Tra cứu thông tin bệnh nhân')
        self.geometry("800x800+10+20")

    def initUI(self):
        # Button
        
        exitBtn=Button(self, text="Thoát", fg='green', font=("Times", 15, "bold italic"), command=self.close_window)
        exitBtn.place(x=LEFTSIDE_START + 650, y=750)

    def load_Data(self):
        conn = sqlite3.connect(databaseFile)
        print("Opened database successfully")

        conn.close()
        print("Data saved!")

    def close_window(self):
        self.destroy()