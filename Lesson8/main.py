import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic
import oop

# xử lý
app = QApplication(sys.argv)
# Khởi tạo database
dtb = oop.UserDatabase()
# Chuyển dữ liệu từ json sang object
dtb.convert_to_object()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lesson8.ui', self)
        # Lấy accout từ file json
        accounts = dtb.get_acc()
        # Thêm danh sách để hiển thị trên listWidget
        self.listWidget.addItems(accounts)
        # Khai báo sự kiện ấn các nút
        self.btn_add.clicked.connect(self.add_item)
        self.btn_edit.clicked.connect(self.edit_item)
        self.btn_delete.clicked.connect(self.delete_item)
        self.btn_search.clicked.connect(self.search_item)

    def add_item(self):
        # Lấy text ở lineEdit
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        # Thêm phần tử vào danh sách / file data
        if username != '' and password != '':
            dtb.add_user(username, password)
        else:
            msg_box('Thêm thất bại', 'Nhập thiếu thông tin')
        # Xóa hết các phần tử trên widget
        self.listWidget.clear()
        # Thêm lại danh sách
        self.listWidget.addItems(dtb.get_acc())
        # Xóa dữ liệu ở lineEdit
        self.lineEdit_username.setText('')
        self.lineEdit_password.setText('')

    def edit_item(self):
        # Lấy index dòng đang chọn trên list widget
        cur = self.listWidget.currentRow()
        # Lấy text ở lineEdit
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        # Thêm phần tử vào danh sách / file data
        if username != '' and password != '':
            if cur >= 0:
                dtb.users_list[cur] = oop.User(username, password)
                dtb.convert_to_dict()
            else:
                msg_box('Lỗi', 'Chưa chọn đối tượng để sửa!')
        else:
            msg_box('Thất bại', 'Nhập thiếu thông tin')
        # Xóa hết các phần tử trên widget
        self.listWidget.clear()
        # Thêm lại danh sách
        self.listWidget.addItems(dtb.get_acc())
        # Xóa dữ liệu ở lineEdit
        self.lineEdit_username.setText('')
        self.lineEdit_password.setText('')

    def delete_item(self):
        # Lấy index dòng đang chọn trên list widget
        cur = self.listWidget.currentRow()
        if cur >= 0:
            dtb.users_list.pop(cur)
            dtb.convert_to_dict()
        else:
            msg_box('Lỗi', 'Chưa chọn đối tượng để xóa!')
        # Xóa hết các phần tử trên widget
        self.listWidget.clear()
        # Thêm lại danh sách
        self.listWidget.addItems(dtb.get_acc())
        # Xóa dữ liệu ở lineEdit
        self.lineEdit_username.setText('')
        self.lineEdit_password.setText('')

    def search_item(self):
        cur = self.listWidget.currentRow()
        # Lấy text ở lineEdit
        username = self.lineEdit_username.text().strip()
        # Khai báo danh sách tìm kiếm
        search_list = []
        check = False
        # Thêm phần tử vào danh sách / file data
        if username != '':
            for user in dtb.users_list:
                if username in user.email:
                    search_list.append(f'{user.email} - {user.password}')
                    check =  True
        else:
            msg_box('Thất bại', 'Nhập thiếu thông tin')
        # Xóa hết các phần tử ở trên widget
        self.listWidget.clear()
        # add lại cả danh sách vào list widget
        if check == True:
            msg_box('Thành công', f'Có {len(search_list)} kết quả!')
        else:
            search_list.append('Không có kết quả')
        self.listWidget.addItems(search_list)
        

def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Run app
window = MainWindow()
window.show()
sys.exit(app.exec())