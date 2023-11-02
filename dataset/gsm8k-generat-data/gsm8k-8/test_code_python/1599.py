def solution():
    total_money = 26
    jumper_cost = 9
    tshirt_cost = 4
    heels_cost = 5

    total_spent = jumper_cost + tshirt_cost + heels_cost
    money_left = total_money - total_spent
    result = money_left
    return result

print(solution())