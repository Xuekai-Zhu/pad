def solution():
    
    initial_money = 20
    price_per_pound = 2
    pounds_of_peaches = 3
    total_cost = price_per_pound * pounds_of_peaches
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())