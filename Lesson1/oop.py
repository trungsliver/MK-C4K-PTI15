# Lập trình hướng đối tượng
# OOP - Object oriented programming

# Tổng quát: OOP là cách mà ta mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Attributre (thuộc tính):  đặc điểm của đối tượng
# Method (phương thức):     hành động của đối tượng

# Khai báo class (Đối tượng tổng quát)
class Human:
    # Hàm khởi tạo
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (attributes)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức - hành động (Method)
    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi")