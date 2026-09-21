radius = float(input())
#求一个圆形的面积
area = 3.14*radius**2
print("面积是%.6f" %area)
#提取面积的整数部分，不要求四舍五入，直接忽略小数
num=int(area)
#分别打印面积的整数部分和小数部分，小数点保留6位
print(num, "%.6f" % (area-num))