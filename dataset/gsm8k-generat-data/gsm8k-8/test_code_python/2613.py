def solution():
    total_money = 87
    beef_price = 5
    cheese_price = 7
    remaining_money = 61

    # Calculate the cost of the beef
    beef_cost = total_money - remaining_money
    beef_weight = beef_cost / beef_price

    # Calculate the cost of the cheese
    cheese_cost = remaining_money
    cheese_weight = cheese_cost / cheese_price
    result = cheese_weight
    return result

print(solution())