def solution():
    ian_winnings = 100
    colin_debt = 20
    helen_debt = 2 * colin_debt
    benedict_debt = helen_debt / 2

    total_debt_paid = colin_debt + helen_debt + benedict_debt
    remaining_money = ian_winnings - total_debt_paid
    result = remaining_money
    return result

print(solution())