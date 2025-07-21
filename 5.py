#กรอกให้ผู้ใช้กด Enter เพื่อออกจากโปรแกรม
print("โปรแกรมตัดเกรดนักเรียน")
input("กด Enter เพื่อออกจากโปรแกรม...")

#กรอกชื่อนักเรียนด้วย
name = input("กรุณาใส่ชื่อนักเรียน: ")

#โปรแกรมตัดเกรด
def calculate_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

#ติดต่อกับผู้ใช้
#ให้กรอกทางแป้นพิมพ์
score = float(input("กรุณาใส่คะแนนของนักเรียน: "))
grade = calculate_grade(score)
print(f"เกรดของนักเรียนคือ: {grade}")

#ถ้าเกรดเป็น A หรือ B ให้แสดงข้อความพิเศษ
if grade in ['A', 'B']:
    print("ยอดเยี่ยม! คุณทำได้ดีมาก!")
else:    print("คุณสามารถทำได้ดีกว่านี้!")

#เก็บข้อมูลคะแนนและชื่อในเกรดในไฟล์
with open('grades.txt', 'a') as file:
    file.write(f"ชื่อ: {name}, คะแนน: {score}, เกรด: {grade}\n")