class Polygon:
    def __init__(self, sides):
        """Khởi tạo với số cạnh của đa giác"""
        self.sides = sides

    def display_sides(self):
        """Hiển thị số cạnh của đa giác"""
        print(f"Đa giác có {self.sides} cạnh.")
class Parallelogram(Polygon):
    def __init__(self, base, height, side):
        """Khởi tạo hình bình hành với cạnh đáy, chiều cao, và cạnh bên"""
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.base = base
        self.height = height
        self.side = side

    def area(self):
        """Tính diện tích hình bình hành"""
        return self.base * self.height

    def perimeter(self):
        """Tính chu vi hình bình hành"""
        return 2 * (self.base + self.side)
class Rectangle(Parallelogram):
    def __init__(self, width, height):
        """Khởi tạo hình chữ nhật với chiều rộng và chiều cao"""
        super().__init__(width, height, width)  # Cạnh bên của hình chữ nhật bằng chiều rộng
        self.width = width
        self.height = height

    def area(self):
        """Tính diện tích hình chữ nhật"""
        return self.width * self.height

    def perimeter(self):
        """Tính chu vi hình chữ nhật"""
        return 2 * (self.width + self.height)
class Square(Rectangle):
    def __init__(self, side):
        """Khởi tạo hình vuông với cạnh bên"""
        super().__init__(side, side)
        self.side = side

    def area(self):
        """Tính diện tích hình vuông"""
        return self.side ** 2

    def perimeter(self):
        """Tính chu vi hình vuông"""
        return 4 * self.side
if __name__ == "__main__":
    # Hình bình hành
    base = float(input("Nhập cạnh đáy hình bình hành: "))
    height = float(input("Nhập chiều cao hình bình hành: "))
    side = float(input("Nhập cạnh bên hình bình hành: "))
    parallelogram = Parallelogram(base, height, side)
    print("Chu vi hình bình hành:", parallelogram.perimeter())
    print("Diện tích hình bình hành:", parallelogram.area())

    # Hình chữ nhật
    width = float(input("Nhập chiều rộng hình chữ nhật: "))
    height = float(input("Nhập chiều cao hình chữ nhật: "))
    rectangle = Rectangle(width, height)
    print("Chu vi hình chữ nhật:", rectangle.perimeter())
    print("Diện tích hình chữ nhật:", rectangle.area())

    # Hình vuông
    side = float(input("Nhập cạnh bên hình vuông: "))
    square = Square(side)
    print("Chu vi hình vuông:", square.perimeter())
    print("Diện tích hình vuông:", square.area())
