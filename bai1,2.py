# bài 1 tính tổng, hiệu , tích , thương hai số bất kì :
import numpy as np
list = [1,2,4,6,8]
print(np.sum(list))
print(np.max(list))
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
