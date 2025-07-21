
#โปรแกรมจำนวนเฉพาะ
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#ติดต่อกับผู้ใช้
#ให้กรอกทางแป้นพิมพ์
number = int(input("กรุณาใส่หมายเลข: "))
if is_prime(number):
    print(f"{number} เป็นจำนวนเฉพาะ")
else:
    print(f"{number} ไม่เป็นจำนวนเฉพาะ")