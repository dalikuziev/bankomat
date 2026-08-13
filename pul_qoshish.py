def pul_qoshish(balans):
    user = input("Qancha pul qo'shmoqchisiz: ")
    if user.isdigit():
        user = int(user)
        balans += user
        print(f"Pul muvaffaqqiyatli qo'shildi, sizning balansingiz {balans} so'm")
    else:
        print("Pul kiriting!")
    return balans
