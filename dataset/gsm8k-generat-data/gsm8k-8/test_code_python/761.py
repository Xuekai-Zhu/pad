def solution():
    total_money = 60
    hummus_cost = 5 * 2
    chicken_cost = 20
    bacon_cost = 10
    veggies_cost = 10
    total_spent = hummus_cost + chicken_cost + bacon_cost + veggies_cost

    remaining_money = total_money - total_spent
    num_apples = remaining_money // 2
    result = num_apples
    return result

print(solution())