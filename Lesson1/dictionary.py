# CRUD: Create - Read - Update - Delete

# Create - khởi tạo
dict1 = {}
dict2 = {
    # Các cặp key - value
    'name': 'Ngọc Huy',
    'age': 15,
    'gender': 'male'
}

# Read - Duyệt, hiện 
    # Duyệt toàn bộ key - value
for key, value in dict2.items():
    print(f"{key}: {value}")
    # Truy cập bằng key
print('Họ tên:', dict2['name'])
    # Sử dụng phương thức get()
print('Họ tên:', dict2.get('name'))
        # Nếu key không tồn tại => None / Giá trị mặc định
print('Money:', dict2.get('money'))
print('Money:', dict2.get('money', '404 not found'))

# Update - chỉnh sửa
    # Thêm cặp key - value
dict2['laptop'] = 'DELL'
    # Chỉnh sửa value
dict2['name'] = 'Huy Quần Hoa'

# Delete - xóa
print(dict2)
    # Xóa theo key - del
del dict2['laptop']
    # Xóa theo key, trả về value - pop()
# dict2.pop('gender')
print(dict2.pop('gender'))
print(dict2)

# Kiểm tra tồn tại key
print('name' in dict2)          # True
print('girlfriend' in dict2)    # False

# Lấy tất cả cặp key - value: items()
print(dict2.items())
# Lấy tất cả key: keys()
print(dict2.keys())
# Lấy tất cả value: values()
print(dict2.values())

# Hàm map(function, itertable)
    # function: hàm biến đổi dữ liệu
    # itertable: bảng dữ liệu

# Ví dụ: Cho danh sách tên học viên trong lớp
# Yêu câu: Dùng map() để thêm tên lớp vào sau tên học sinh
arr = ['Huy', 'An', 'Giang', 'Ngọc', 'Nam']
    # Cách 1: Dùng hàm xác định
def convert_name(student):
    return student + ' PTI15'
arr1 = map(convert_name, arr)
print(list(arr1))

    # Cách 2: Dùng lambda - hàm ẩn danh / không xác định
arr2 = map(lambda name: name + ' PTI15', arr)
print(list(arr1))

        # Giải thích cách 2
arr3 = []
for name in arr:
    new_name = name + ' PTI15'
    arr3.append(new_name)
print(arr3)

# Bài tập: Cho 1 danh sách điểm hệ số 10 (thang điểm 10)
# Yêu cầu: dùng map() để chuyển đổi toàn bộ phần tử danh sách sang điểm hệ số 4 (thang 4)
gpa_10 = [5, 7, 8, 10, 9]
    # Cách 1: Dùng hàm xác định
def convert_gpa(score):
    return score / 10 * 4
gpa_4 = map(convert_gpa, gpa_10)
print(list(gpa_4))

    # Cách 2: Dùng làm không xác định
gpa_4 = map(lambda gpa: gpa / 10 * 4, 2, gpa_10)
print(list(gpa_4))
