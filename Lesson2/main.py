# DICTIONARY & MAP
# Bài 1: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
# Ví dụ: tRunG -> TRUNG
pti15 = ['nGoC', 'dUNg', 'naM', 'aN', 'GiANg']
    # cách 1:
def convert_name(name):
    return name.upper()
pti15_1 = list(map(convert_name, pti15))
print(pti15_1)
    # cách 2:
pti15_2 = list(map(lambda name: name.upper(), pti15))
print(pti15_2)

# Bài 2: Quản lý thông tin sinh viên
# #Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    "name": "John",
    "age": 22,
    "grade": "A"
}
# 2. Cập nhật grade của sinh viên thành "A+".
student["grade"] = "A+"
# 3. Xóa thông tin age của sinh viên.
del student["age"]
# 4. Kiểm tra xem name có trong dictionary không.
print('name' in student)

# Bài 3: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'
def count_words(sentence):
    # strip(): xóa khoảng trắng ở đầu và cuối
    # split(): tách chuỗi thành list các từ (danh sách)
    words = sentence.strip().split()
    # Khởi tạo dictionary để lưu dữ liệu
    word_count = {}
    # Duyệt qua danh sách các từ
    for word in words:
        # Nếu từ đã có trong dictionary, tăng số lần xuất hiện lên 1
        if word in word_count:
            word_count[word] += 1
        # Từ chưa có trong dictionary
        else:
            word_count[word] = 1
    return word_count
print(count_words(sentence))

# Bài 4: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}
def merge_dicts(dict1, dict2):
    # Tạo bản sao của dict1 để không bị thay đổi dữ liệu
    result = dict1.copy()
    # Duyệt qua các key và giá trị của dict2
    for key, value in dict2.items():
        # Nếu key đã có trong result, cộng giá trị  
        if key in result:
            result[key] += value
        # Nếu key chưa có trong result, thêm vào result
        else:
            result[key] = value
    return result
print(merge_dicts(A, B))

# Bài 5: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
def find_max_key(dict):
    # Khai báo value, key lớn nhất là phần tử đầu tiên trong dict
    max_value = list(dict.values())[0]
    max_key = list(dict.keys())[0]
    # Duyệt qua các key và value trong dict
    for key, value in dict.items():
        # Nếu value lớn hơn max_value, cập nhật max_value và max_key
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
print(find_max_key(A))
print(find_max_key(B))

# Bài 6: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.
grade = {
    'Minh Ngọc': 9,
    'Tiến Dũng': 7,
    'Hoàng Nam': 8,
    'Hiếu An': 8.5,
    'Trường Giang': 7.5
}
def sort_dict(dictionary):
    # sử dụng sorted() với key để sắp xếp dictionary
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
print(sort_dict(grade))

# Bài 7: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.
data = {
    'apple': 1,
    'banana': 2,
    'cherry': 2,
    'bomb': 3,
    'elderberry': 3
}
def group_by_value(dict):
    # Khai báo một dictionary để lưu trữ các phần tử nhóm
    result = {}
    # Duyệt qua các key và value trong dict
    for key, value in dict.items():
        # Nếu value chưa có trong result, thêm vào
        if value not in result:
            result[value] = []
        # Nếu value đã có trong result, thêm key vào danh sách
        result[value].append(key)
    return result
print(group_by_value(data))


# Bài 8: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
def list_to_dict(keys, values):
    # zip(): tạo ra các cặp key-value từ 2 danh sách
    # dict(): chuyển các cặp key-value thành dictionary
    return dict(zip(keys, values))
print(list_to_dict(keys, values))