import math

class Triangle:
    def __init__(self, side1, side2, side3):
        """Khởi tạo tam giác với ba cạnh"""
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        """Tính chu vi tam giác"""
        return self.side1 + self.side2 + self.side3

    def area(self):
        """Tính diện tích tam giác bằng công thức Heron"""
        s = self.perimeter() / 2  # Nửa chu vi
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def display(self):
        """Hiển thị các thông tin của tam giác"""
        print(f"Cạnh 1: {self.side1}, Cạnh 2: {self.side2}, Cạnh 3: {self.side3}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area():.2f}")
class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side, base):
        """Khởi tạo tam giác cân với hai cạnh bằng nhau (equal_side) và cạnh đáy (base)"""
        super().__init__(equal_side, equal_side, base)

    def display(self):
        """Hiển thị thông tin của tam giác cân"""
        print("Đây là tam giác cân:")
        super().display()
class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        """Khởi tạo tam giác đều với ba cạnh bằng nhau"""
        super().__init__(side, side)  # Cả ba cạnh đều bằng nhau trong tam giác đều

    def display(self):
        """Hiển thị thông tin của tam giác đều"""
        print("Đây là tam giác đều:")
        super().display()
class RightTriangle(Triangle):
    def __init__(self, side1, side2):
        """Khởi tạo tam giác vuông với hai cạnh góc vuông (side1, side2)"""
        hypotenuse = math.sqrt(side1**2 + side2**2)  # Tính cạnh huyền
        super().__init__(side1, side2, hypotenuse)

    def display(self):
        """Hiển thị thông tin của tam giác vuông"""
        print("Đây là tam giác vuông:")
        super().display()
if __name__ == "__main__":
    # Tam giác cân
    equal_side = float(input("Nhập cạnh bằng nhau của tam giác cân: "))
    base = float(input("Nhập cạnh đáy của tam giác cân: "))
    isosceles_triangle = IsoscelesTriangle(equal_side, base)
    isosceles_triangle.display()

    # Tam giác đều
    side = float(input("Nhập cạnh của tam giác đều: "))
    equilateral_triangle = EquilateralTriangle(side)
    equilateral_triangle.display()

    # Tam giác vuông
    side1 = float(input("Nhập cạnh góc vuông thứ nhất: "))
    side2 = float(input("Nhập cạnh góc vuông thứ hai: "))
    right_triangle = RightTriangle(side1, side2)
    right_triangle.display()
