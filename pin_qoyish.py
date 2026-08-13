def pin_qoyish():
    while True:
        pin = input("Parol qo'ying: ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        else:
            print("Parol qonunga zid, qayta qo'ying!")
