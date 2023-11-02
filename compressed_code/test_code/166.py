def solution():
    
    total_money = 100
    colin_paid = 20
    helen_paid = 2 * colin_paid
    benedict_paid = helen_paid / 2
    total_debt_paid = colin_paid + helen_paid + benedict_paid
    money_left = total_money - total_debt_paid
    result = money_left
    return result

print(solution())