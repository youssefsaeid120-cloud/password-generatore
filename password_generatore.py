import random
import string

print("Welcome to the Password Generator!")

while True:
    # استقبال الطول الإجمالي وعدد كل نوع من المكونات
    length = int(input("\nEnter the total length of the password: "))
    capital = int(input("How many CAPITAL letters?: "))
    small = int(input("How many small letters?: "))
    number = int(input("How many numbers?: "))
    symbol = int(input("How many symbols?: "))

    # التحقق من أن مجموع الأجزاء يساوي الطول الإجمالي تماماً
    if length == (capital + small + number + symbol):
        # توليد كل جزء من المكونات المحددة بدقة
        cap_part = random.choices(string.ascii_uppercase, k=capital)
        small_part = random.choices(string.ascii_lowercase, k=small)
        num_part = random.choices(string.digits, k=number)
        
        # استخدام رموز آمنة وشائعة الاستخدام في المواقع
        safe_symbols = "!@#$%^&*()_+-="
        sym_part = random.choices(safe_symbols, k=symbol)
        
        # دمج كل المكونات في قائمة واحدة
        password_list = cap_part + small_part + num_part + sym_part
        
        # خلط القائمة عشوائياً لضمان عدم ترتيبها (حروف ثم أرقام ثم رموز)
        random.shuffle(password_list)
        
        # تحويل القائمة إلى نص واحد (String)
        generated_password = "".join(password_list)
        
        print(f"\nPassword Generated Successfully: {generated_password}")
        break  # الخروج من الـ Loop بعد النجاح
    else:
        print("\n[Error] The sum of components does not match the total length. Please try again!")
