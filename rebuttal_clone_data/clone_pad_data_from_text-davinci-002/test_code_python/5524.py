def solution():
    money_earned_phone = 10
    money_earned_laptop = 20
    phones_repaired_Monday = 3
    phones_repaired_Tuesday = 5
    laptops_repaired_Wednesday = 2
    laptops_repaired_Thursday = 4
    total_money_earned = (money_earned_phone * (phones_repaired_Monday + phones_repaired_Tuesday)) + (money_earned_laptop * (laptops_repaired_Wednesday + laptops_repaired_Thursday))
    result = total_money_earned
    return result

print(solution())