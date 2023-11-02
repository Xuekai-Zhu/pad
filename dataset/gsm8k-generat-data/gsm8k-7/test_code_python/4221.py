def solution():
    initial_money = 100
    roast_cost = 17
    veggie_cost = 11

    # Calculate the total amount spent
    total_spent = roast_cost + veggie_cost

    # Calculate the remaining money
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())