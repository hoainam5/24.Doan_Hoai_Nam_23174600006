class Rectangle:
    def __init__(self):
        self.length = float(input("Nhập chiều dài của hình chữ nhật: "))
        self.width = float(input("Nhập chiều rộng của hình chữ nhật: "))

    # Phương thức tính chu vi
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    # Phương thức tính diện tích
    def calculate_area(self):
        return self.length * self.width

    # Phương thức in thông tin hình chữ nhật
    def display_info(self):
        print(f"Chiều dài: {self.length}")
        print(f"Chiều rộng: {self.width}")
        print(f"Chu vi: {self.calculate_perimeter()}")
        print(f"Diện tích: {self.calculate_area()}")

# Chương trình chính
rect = Rectangle()
rect.display_info()
