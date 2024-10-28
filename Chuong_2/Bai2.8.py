import json

if __name__ == "__main__":
    # Đối tượng Python mẫu (dictionary)
    python_object = {
        "name": "Peter",
        "age": 23,
        "city": "England",
        "is_student": False,
        "grades": [95, 89, 78]
    }

    # Chuyển đổi đối tượng Python thành chuỗi JSON và in ra
    json_string = json.dumps(python_object, indent=2)
    print("Chuỗi JSON sau khi chuyển đổi:")
    print(json_string)