from balans_korish import balans_korish
from pin_tekshirish import pin_tekshirish
from pin_ozgartirish import pin_ozgartirish
from pin_qoyish import pin_qoyish
from pul_qoshish import pul_qoshish
from pul_yechish import pul_yechish

def bankomat():
    balans = 0
    pin = pin_qoyish()
    if not pin_tekshirish(pin):
        return "Tizimga kirish rad etildi."
    print("Bankamatga xush kelibsiz")
    with open("check.txt", "w"):
        pass
    while True:
        print("Menu:\n"
              "1. Balans ko'rish\n"
              "2. Pul qo'shish\n"
              "3. Pul yechish\n"
              "4. Parolni o'zgartirish\n"
              "5. Chiqish")
        amal = input("Amal tanlang: ")
        if amal == "1":
            balans = balans_korish(balans)
            with open("check.txt", "a") as file:
                file.write(f"Sizning balansingiz: {balans} so'm\n")
        elif amal == "2":
            balans = pul_qoshish(balans)
            with open("check.txt", "a") as file:
                file.write(f"Pul muvaffaqqiyatli qo'shildi, sizning balansingiz {balans} so'm\n")
        elif amal == "3":
            balans = pul_yechish(balans)
            with open("check.txt", "a") as file:
                file.write(f"Pul muvaffaqqiyatli yechildi, sizning balansingiz: {balans} so'm\n")
        elif amal == "4":
            pin = pin_ozgartirish(pin)
            with open("check.txt", "a") as file:
                file.write(f"Parol {pin} ga muvaffaqqiyatli o'zgartirildi.\n")
        elif amal == "5":
            return "Tizimdan chiqdingiz, Xayr!"
        else:
            print("Xato amal, 1-5 orasidan tanlang!")
