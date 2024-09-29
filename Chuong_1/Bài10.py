class Point:
    def __init__(self, x=0, y=0):
        """Khởi tạo điểm trong mặt phẳng tọa độ với giá trị mặc định (0, 0)."""
        self.x = x
        self.y = y

    def display(self):
        """Hiển thị tọa độ điểm."""
        print(f"Điểm có tọa độ: ({self.x}, {self.y})")
import math

class Ellipse(Point):
    def __init__(self, x, y, major_axis, minor_axis):
        """Khởi tạo elip với tọa độ tâm (x, y), bán trục lớn (major_axis) và bán trục nhỏ (minor_axis)."""
        super().__init__(x, y)  # Kế thừa tọa độ điểm
        self.major_axis = major_axis  # Bán trục lớn
        self.minor_axis = minor_axis  # Bán trục nhỏ

    def area(self):
        """Tính diện tích elip."""
        return math.pi * self.major_axis * self.minor_axis

    def display(self):
        """Hiển thị thông tin về elip."""
        super().display()
        print(f"Bán trục lớn: {self.major_axis}")
        print(f"Bán trục nhỏ: {self.minor_axis}")
        print(f"Diện tích elip: {self.area():.2f}")
class Circle(Ellipse):
    def __init__(self, x, y, radius):
        """Khởi tạo đường tròn với tâm (x, y) và bán kính (radius)."""
        super().__init__(x, y, radius, radius)  # Bán trục lớn và bán trục nhỏ bằng nhau

    def display(self):
        """Hiển thị thông tin về đường tròn."""
        print("Đây là một đường tròn:")
        super().display()  # Hiển thị các thuộc tính từ lớp Elip
        print(f"Bán kính: {self.major_axis}")
        print(f"Diện tích đường tròn: {self.area():.2f}")
if __name__ == "__main__":
    # Nhập thông tin cho elip
    x = float(input("Nhập tọa độ x của tâm elip: "))
    y = float(input("Nhập tọa độ y của tâm elip: "))
    major_axis = float(input("Nhập bán trục lớn của elip: "))
    minor_axis = float(input("Nhập bán trục nhỏ của elip: "))
    
    # Tạo đối tượng elip và tính diện tích
    ellipse = Ellipse(x, y, major_axis, minor_axis)
    ellipse.display()

    # Nhập thông tin cho đường tròn
    x = float(input("Nhập tọa độ x của tâm đường tròn: "))
    y = float(input("Nhập tọa độ y của tâm đường tròn: "))
    radius = float(input("Nhập bán kính của đường tròn: "))

    # Tạo đối tượng đường tròn và tính diện tích
    circle = Circle(x, y, radius)
    circle.display()
