def add_numbers(a, b):
    sum = a + b
    return sum

#ติดต่อกับผู้ใช้
#ให้กรอกทางแป้นพิมพ์
num1 = int(input("กรุณาใส่หมายเลขแรก: "))
num2 = int(input("กรุณาใส่หมายเลขที่สอง: "))
result = add_numbers(num1, num2)
print(f"ผลบวกของ {num1} และ {num2} คือ {result}")