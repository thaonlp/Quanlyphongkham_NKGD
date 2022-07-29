import sqlite3
from tkinter import *
from tkinter import messagebox

# add widgets here
LEFTSIDE_START = 10
LABEL_LENGTH = 150

databaseFile = "hsbn.db"
#  Table columns of BenhNhan ['index', 'ID', 'FIRSTNAME', ' FULLNAME', 'BIRTH', 'ADDRESS', 'NOTE', 'SEX', 'JOB', 'PHONE']
class PatientLookUp(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = StringVar()
        self.birth = IntVar()
        self.phone = StringVar()
        self.variable_text_map = {
            "Tên": self.name,
            "Năm sinh": self.birth,
            "Số điện thoại": self.phone,
        }

        mainlbl=Label(self, text="Thông tin bệnh nhân", fg='red', font=("Helvetica", 28, "bold italic"))
        mainlbl.place(x=LEFTSIDE_START + 300, y=5)

        self.initUI()
        self.title('Nha khoa Gia Định - Tra cứu thông tin bệnh nhân')
        self.geometry("800x800+10+20")

    def initUI(self):
        # Button
        findBtn = Button(self, text="Tìm bệnh nhân", fg='green', font=("Times", 15, "bold italic"), command=self.query_from_BenhNhan)
        findBtn.place(x=LEFTSIDE_START + 330, y=750)
        exitBtn = Button(self, text="Thoát", fg='green', font=("Times", 15, "bold italic"), command=self.close_window)
        exitBtn.place(x=LEFTSIDE_START + 650, y=750)
        # Label and Textbox
        self.create_window_label_with_entry("Tên", LEFTSIDE_START, 50)
        self.create_window_label_with_entry("Năm sinh", LEFTSIDE_START, 80)
        self.create_window_label_with_entry("Số điện thoại", LEFTSIDE_START, 110)

    def create_window_label_with_entry(self, text, x, y):
        lbl=Label(self, text=text, fg='blue', font=("Times", 15))
        lbl.place(x=x, y=y)
        txtfld=Entry(self, text=self.variable_text_map[text], bd=3)
        txtfld.place(x=x+LABEL_LENGTH,y=y)

    def query_from_BenhNhan(self):
        name = self.variable_text_map["Tên"].get()
        query_name = name.upper()
        birth = self.variable_text_map["Năm sinh"].get()
        query_birth = str(birth)
        phone = self.variable_text_map["Năm sinh"].get()
        query_phone = str(phone)
        con = sqlite3.connect(databaseFile)
        query = "SELECT ID,FULLNAME,BIRTH FROM BenhNhan WHERE FIRSTNAME = '" + query_name + "' AND BIRTH = '" + query_birth + "';"
        print("Query cmd: ", query)
        cursorObj = con.cursor()
        cursorObj.execute(query)
        results = cursorObj.fetchall()
        #df = pd.read_sql(query, con)
        print("Query database when name is ", query_name)
        #query1 = con.execute("SELECT * From BenhNhan")
        #colsBN = [column[0] for column in query1.description]
        # print(colsBN)
        listbox = Listbox(self)
        for result in results:
            listbox.insert(END, result)
            # print(result)
        # messagebox.showinfo("Kết quả tìm kiếm", result)
        listbox.pack(fill=BOTH, expand=YES)
        con.close()

    def close_window(self):
        self.destroy()
