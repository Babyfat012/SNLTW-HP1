def main():
    username = "admin"
    password = "123"

    # Chức năng đăng nhập
    while True:
        input_username = input("\tNhập tài khoản: ").strip()
        input_password = input("\tNhập mật khẩu: ").strip()
        
        if input_username == username and input_password == password:
            print("\tĐăng nhập thành công!")
            break
        else:
            print("\tTài khoản hoặc mật khẩu không đúng. Vui lòng thử lại.")

    laptops = []
    next_id = 1  # Khởi tạo ID bắt đầu từ 1

    while True:
        # Tạo viền cho giao diện menu
        menu = "\n\t" + "-" * 40 + "\n"
        menu += "\t--- QUẢN LÝ CỬA HÀNG LAPTOP ---\n"
        menu += "\t1. Thêm sản phẩm\n"
        menu += "\t2. Sửa sản phẩm\n"
        menu += "\t3. Xóa sản phẩm\n"
        menu += "\t4. Tìm kiếm sản phẩm\n"
        menu += "\t5. Danh sách sản phẩm\n"
        menu += "\t0. Thoát\n"
        menu += "\t" + "-" * 40

        print(menu)

        choice = input("\tChọn chức năng (0-5): ").strip()

        if choice == '1':
            # Tạo laptop mới với ID tự động
            name = input("\tNhập tên laptop: ").strip().capitalize()
            brand = input("\tNhập thương hiệu laptop: ").strip().capitalize()
            price = float(input("\tNhập giá laptop: ").strip())
            quantity = int(input("\tNhập số lượng laptop: ").strip())  # Nhập số lượng
            laptops.append({'id': next_id, 'name': name, 'brand': brand, 'price': price, 'quantity': quantity})
            print("\tLaptop đã được thêm thành công với ID:", next_id)
            next_id += 1  # Tăng ID cho laptop tiếp theo

        elif choice == '2':
            id = int(input("\tNhập ID laptop cần sửa: ").strip())
            for laptop in laptops:
                if laptop['id'] == id:
                    laptop['name'] = input("\tNhập tên laptop mới: ").strip().capitalize()
                    laptop['brand'] = input("\tNhập thương hiệu laptop mới: ").strip().capitalize()
                    laptop['price'] = float(input("\tNhập giá laptop mới: ").strip())
                    laptop['quantity'] = int(input("\tNhập số lượng mới: ").strip())  # Nhập số lượng mới
                    print("\tLaptop đã được sửa thành công.")
                    break
            else:
                print("\tKhông tìm thấy laptop với ID đó.")

        elif choice == '3':
            id = int(input("\tNhập ID laptop cần xóa: ").strip())
            for laptop in laptops:
                if laptop['id'] == id:
                    laptops.remove(laptop)
                    print("\tLaptop đã được xóa thành công.")
                    break
            else:
                print("\tKhông tìm thấy laptop với ID đó.")

        elif choice == '4':
            id = int(input("\tNhập ID laptop cần tìm: ").strip())
            found = False
            for laptop in laptops:
                if laptop['id'] == id:
                    found = True
                    price_display = int(laptop['price']) if laptop['price'].is_integer() else laptop['price']
                    print(f"\tTìm thấy laptop: ID: {laptop['id']}, Tên: {laptop['name']}, Thương hiệu: {laptop['brand']}, Giá: {price_display}, Số lượng: {laptop['quantity']}")
                    break
            if not found:
                print("\tKhông tìm thấy laptop với ID đó.")

        elif choice == '5':
            if not laptops:
                print("\tChưa có laptop nào trong cửa hàng.")
            else:
                print("\n\t" + "-" * 70)
                print("\t| {:<5} | {:<20} | {:<15} | {:<10} | {:<10} |".format("ID", "Tên", "Thương hiệu", "Giá", "Số lượng"))
                print("\t" + "-" * 70)
                for laptop in laptops:
                    price_display = int(laptop['price']) if laptop['price'].is_integer() else laptop['price']
                    print("\t| {:<5} | {:<20} | {:<15} | {:<10} | {:<10} |".format(laptop['id'], laptop['name'], laptop['brand'], price_display, laptop['quantity']))
                print("\t" + "-" * 70)

        elif choice == '0':
            print("\tThoát chương trình.")
            break

        else:
            print("\tLựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
