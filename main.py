from medical_report import *
from database_lookup import *
from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x1000')
        self.title('Nha khoa Gia Định - 123A Lê Văn Duyệt, Phường 3, Quận Bình Thạnh, TPHCM')
        mainlbl=Label(self, text="Chương trình quản lý bệnh nhân", fg='red', font=("Times", 28, "bold italic"))
        mainlbl.place(x=LEFTSIDE_START + 300, y=5)
        lb1=Label(self, text="Tạo phiếu khám bệnh", fg='blue', font=("Times", 15, "bold"))
        lb1.place(x=LEFTSIDE_START, y=100)
        newReport = Button(self, text='Tạo phiếu mới',command=self.create_new_medical_report)
        newReport.place(x=LEFTSIDE_START + 300, y=100 - 5)
        lb2=Label(self, text="Tìm bệnh nhân", fg='blue', font=("Times", 15, "bold"))
        lb2.place(x=LEFTSIDE_START, y=130)
        findPatient = Button(self, text='Tìm bệnh nhân cũ',command=self.look_for_patient)
        findPatient.place(x=LEFTSIDE_START + 300, y=130 - 5)


    def create_new_medical_report(self):
        newWindow = MedicalReport(self)
        newWindow.grab_set()

    def look_for_patient(self):
        print("Searching in database")
        newWindow = PatientLookUp(self)
        newWindow.grab_set()

def main(): 
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
