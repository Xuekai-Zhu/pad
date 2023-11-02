def solution():
    
    initial_amount = 55
    shirt_cost = 7
    other_shop_cost = 3 * shirt_cost
    total_spent = shirt_cost + other_shop_cost
    money_left = initial_amount - total_spent
    result = money_left
    return result

print(solution())