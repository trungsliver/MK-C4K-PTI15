import oop

# Khởi tạo dữ liệu (database)
dtb = oop.PlayerDatabase()

# Load data vào danh sách object
dtb.convert_to_object()

# Kiểm tra dữ liệu
print("players_dict:", len(dtb.players_dict))
print("players_list:", len(dtb.players_list))
# dtb.show_all()

# Test hàm tìm kiếm theo tên
find1 = dtb.find_player_by_name("Cristiano Ronaldo")
    # Tìm thấy
if find1 != False:
    print(find1.show_info())
else:
    print("Không tìm thấy player nào")

find2 = dtb.find_player_by_name("Tien Dung")
    # Không tìm thấy
if find2 != False:
    print(find2.show_info())
else:
    print("Không tìm thấy player nào")

# Thêm 1 data mới
new_player = {
        "id": 16,
        "name": "Ngoc Huy",
        "dob": "28/01/2010",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 1
}
dtb.add_player(new_player)

# Sửa thông tin
edit_player = {
        "id": 16,
        "name": "Ngoc Huy hihi",
        "dob": "28/01/2010",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 1
}
dtb.edit_player('Ngoc Huy', edit_player)

# Xóa thông tin
dtb.delete_player('Ngoc Huy')