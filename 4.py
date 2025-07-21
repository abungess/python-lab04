#โปรแกรมหาพื้นที่สี่เหลี่ยมผืนผ้า
def calculate_area_rectangle(width, height):
    area = width * height
    return area
#ติดต่อกับผู้ใช้
#ให้กรอกทางแป้นพิมพ์
width = float(input("กรุณาใส่ความกว้างของสี่เหลี่ยมผืนผ้า: "))
height = float(input("กรุณาใส่ความสูงของสี่เหลี่ยมผืนผ้า: "))
area = calculate_area_rectangle(width, height)
print(f"พื้นที่ของสี่เหลี่ยมผืนผ้าคือ {area} ตารางหน่วย")   