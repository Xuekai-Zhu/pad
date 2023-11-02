def solution():
    johns_money = 200
    johns_mother_money = johns_money * (3/8)
    johns_father_money = johns_money * (3/10)

    money_spent = johns_mother_money + johns_father_money
    money_left = johns_money - money_spent
    result = money_left
    return result

print(solution())