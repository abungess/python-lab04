def convert_toBE(year):
    print(f"ปี ค.ศ. {year} เป็นปี พ.ศ. = {year + 543}")
def convert_toCE(year):
    print(f"ปี พ.ศ. {year} เป็นปี ค.ศ. = {year - 543}")

convert_toBE(2000)

convert_toCE(2568)

def celsius_to_fahrenheit(c):
    """แปลงเซลเซียสเป็นฟาเรนไฮต์"""
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    """แปลงฟาเรนไฮต์เป็นเซลเซียส"""
    return (f - 32) * 5/9

# เมนูโปรแกรม
while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("0. Exit")
    choice = input("Choose menu: ").strip()
    if choice == '1':
        c = float(input("Enter Celsius: "))
        print(f"{c} °C = {celsius_to_fahrenheit(c):.2f} °F")
    elif choice == '2':
        f = float(input("Enter Fahrenheit: "))
        print(f"{f} °F = {fahrenheit_to_celsius(f):.2f} °C")
    elif choice == '0':
        print("Goodbye!")
        break
    else:
        print("Invalid menu. Please try again.")