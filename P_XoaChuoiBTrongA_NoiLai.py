def remove_substring(a, b):
    while b in a:
        a = a.replace(b, "", 1)
    return a

a = input("Nhập chuỗi a : ")
b = input("Nhập chuỗi b : ")

a = remove_substring(a, b)

print("Chuỗi a sau khi xóa chuỗi b : ", a)

