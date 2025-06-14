import os, json

# Xem đường dẫn thư mục
# print(os.getcwd())

# Đọc dữ liệu
def load_json_data():
    dict_data = list()
    # with open(): dùng để mở file, tự động đóng sau khi thực hiện
    # 'r': thao tác đọc file
    with open('data.json', 'r') as file:
        data = json.load(file)
    dict_data.extend(data)
    return dict_data

# Ghi dữ liệu
def write_json_data(json_data):
    with open('data.json', 'w') as file:
        json.dump(json_data, file)