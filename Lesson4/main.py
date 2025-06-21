import oop

# Khởi tạo dữ liệu (database)
dtb = oop.PlayerDatabase()

# Load data vào danh sách object
dtb.convert_to_object()

# Kiểm tra dữ liệu
print("players_dict:", len(dtb.players_dict))
print("players_list:", len(dtb.players_list))
dtb.show_all()