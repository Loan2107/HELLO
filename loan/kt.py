print("Nhap So Luong Sinh Vien: ")
n = int(input())
ds = {"MSSV":"", "Ho Va Ten":""}
li = []
for i in range(1,n+1):
    print("Nhap MSSV:")
    m = str(input())
    ds["MSSV"] = m
    li.append(ds)

for i in li:
    print("Danh sach sinh vien la: ")
    print(i["MSSV"]) 
