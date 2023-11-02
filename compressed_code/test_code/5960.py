def solution():
    
    initial_money = 100
    colin_debt = 20
    helen_debt = 2 * colin_debt
    benedict_debt = helen_debt / 2
    total_debt = colin_debt + helen_debt + benedict_debt
    remaining_money = initial_money - total_debt
    result = remaining_money
    return result

print(solution())