def parol_tekshirish(pin):
    imkon = 3
    while imkon > 0:
        user = input("Parolni kiriting: ")
        if user == pin:
            print("Parol to'g'ri")
            return True
        else:
            imkon -= 1
            print("Parol xato")
    print("Karta bloklandi!")
    return False
