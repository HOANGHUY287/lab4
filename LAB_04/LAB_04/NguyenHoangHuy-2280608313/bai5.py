SoGioLam = float(input("Nhập số giờ làm trong tuần: "))
LuongGio = float(input("Nhập số lương theo giờ làm tiêu chuẩn: "))
GioTieuChuan = 48
GioVuotChuan = max(0, SoGioLam - GioTieuChuan)
LuongVeTay = GioTieuChuan * LuongGio + GioVuotChuan * LuongGio * 1.5
print(f"Số tiền lương của nhân viên nhận được là: {LuongVeTay}" )