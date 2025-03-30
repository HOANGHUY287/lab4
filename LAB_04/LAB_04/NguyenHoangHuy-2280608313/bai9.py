def kiem_tra_so_nguyen_to(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(n):
    print("Là số nguyên tố.")
else:
    print("Không phải là số nguyên tố.")