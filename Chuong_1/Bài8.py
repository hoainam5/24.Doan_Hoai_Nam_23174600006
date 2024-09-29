class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In ra thông tin về ngày, tháng, năm."""
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        """Tính ngày tiếp theo và cập nhật."""
        # Số ngày của mỗi tháng (tháng 2 có thể có 28 hoặc 29 ngày)
        days_in_month = [31, 29 if self.is_leap_year(self.year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Kiểm tra nếu đã hết tháng
        if self.day < days_in_month[self.month - 1]:
            self.day += 1
        else:
            self.day = 1
            if self.month == 12:  # Nếu hết tháng 12 thì sang năm mới
                self.month = 1
                self.year += 1
            else:  # Chuyển sang tháng tiếp theo
                self.month += 1

    def is_leap_year(self, year):
        """Kiểm tra xem năm có phải là năm nhuận không."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name
        self.birth_date = birth_date
        self.hire_date = hire_date

    def display(self):
        """Hiển thị thông tin nhân viên."""
        print(f"Tên nhân viên: {self.name}")
        print("Ngày sinh:", end=" ")
        self.birth_date.display()  # Gọi phương thức display của lớp Date
        print("Ngày vào công ty:", end=" ")
        self.hire_date.display()  # Gọi phương thức display của lớp Date
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        """Thêm nhân viên vào hệ thống."""
        self.employees.append(employee)

    def list_employees(self):
        """Liệt kê tất cả nhân viên trong công ty."""
        for employee in self.employees:
            employee.display()
            print("-" * 30)

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo các đối tượng Date cho ngày sinh và ngày vào công ty
    birth_date = Date(15, 5, 1990)
    hire_date = Date(1, 3, 2020)
    
    # Tạo đối tượng Employee
    employee1 = Employee("Nguyễn Văn A", birth_date, hire_date)
    
    # Tạo hệ thống quản lý nhân viên
    ems = EmployeeManagementSystem()
    
    # Thêm nhân viên vào hệ thống
    ems.add_employee(employee1)
    
    # Tạo thêm nhân viên khác
    birth_date2 = Date(20, 7, 1985)
    hire_date2 = Date(10, 1, 2015)
    employee2 = Employee("Trần Thị B", birth_date2, hire_date2)
    ems.add_employee(employee2)
    
    # Liệt kê thông tin các nhân viên
    ems.list_employees()
