# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:41:55 2022

@author: USER
"""

import pandas as pd
import numpy as np
df = pd.DataFrame()
#print(df)
#display(df)
lst = ['kế toán', 'kinh doanh', 'tiếp thị']
df = pd.DataFrame(lst)
#print(df)
#tuples = [('kế toán',2000),('kinh doanh',2100),('kinh doanh',2100)]
#df = pd.DataFrame(tuples, columns= ['nghề','lương']
#print(df)
# Tạo DataFrame từ Tuple:
# Khai báo Tuple:
tuples = [('Kế toán', 2000),('Kinh doanh', 2100), ('Tiếp thị', 1900)]
# Gán giá trị của Tuple vào DataFrame
df = pd.DataFrame(tuples, columns=['Nghề','Lương'])
#print(df)
# Tạo DataFrame từ Dictionary :
# Khai báo Dictionary :
dic = {'Công việc':['Kỹ sư','Bác sĩ','Giáo viên'],\
       'Thu nhập':[3000, 3100, 2900]}
# Gán giá trị của Dictionary vào DataFrame
df = pd.DataFrame(dic)
#print(df)
# Tạo Series từ Dictionary
# Khai báo Dictionary:
dict = {0 : 'Kế toán', 1 : 'Kinh doanh', 2 : 'Tiếp thị'}
# Gán giá trị của Dictionary vào Series
seri = pd.Series(dict)
#print(seri)
df.info()
# Tạo Series từ Numpy array
# Tạo Numpy array
arr = np.array([51,65,48,59,68])
# Gán giá trị của array vào Series
seri2 = pd.Series(arr)
#print(seri2)
# Tạo series từ các giá trị vô hướng
# Tạo Series
seri = pd.Series(10, index=[0,1,2,3,4,5])
seri = pd.Series(np.NaN, index=[0,1,2,3,4,5])
# seri = pd.Series(np.arange(1,18,2))
#print(seri)
# Nhập dữ liệu
data = pd.read_csv('C:\Users\USER\Desktop\DA30092022\FoodPrice_in_Turkey.csv',ArithmeticErrorheader=0)
#print('*'*20, "Nhập dữ liệu thành công", '*'*20)
print(data)
# data2 = pd.read_csv('FoodPrice_in_Turkey.csv', header = 0, encoding = 'utf-8')
# display(data2)





