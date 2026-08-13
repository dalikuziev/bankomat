def pul_yechish(balans):
    user = input("Qancha pul yechmoqchisiz: ")
    if user.isdigit():
        user = int(user) * 1.01
        if user < balans:
            balans -= user
            print(f"Pul muvaffaqqiyatli yechildi, sizning balansingiz: {balans} so'm")
        else:
            print("Balans yetarli emas!")
    else:
        print("Pul kiriting!")
    return balans
