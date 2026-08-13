def pin_ozgartirish(pin):
    user = input("Eski parolni kiriting: ")
    if user == pin:
        new_user = input("Yangi parolni kiriting: ")
        if new_user.isdigit() and len(new_user) == 4:
            new_user2 = input("Yangi parolni tasdiqlang: ")
            if new_user == new_user2:
                print(f"Parol {new_user} ga muvaffaqqiyatli o'zgartirildi.")
                return new_user
            print("Parollar mos kelmadi")
            return pin
        print("Parol 4 xonali raqam bo'lishi shart!")
        return pin
    print("Eski parol xato!")
    return pin
