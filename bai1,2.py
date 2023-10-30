# bài 1 tính tổng, hiệu , tích , thương hai số bất kì :
print(123)
try:
    a = int(input('hay nhap a:'))
    b = int(input('hay nhap b:'))
    print('tong = ', a+b)
    print('hieu =',a-b)
    print('tich =',a*b)
    print('thuong = ',a/b)
except:
    print(' du lieu nhap khong dung')
    print("abc")
finally:
    print('ket thuc chuong trinh!')
