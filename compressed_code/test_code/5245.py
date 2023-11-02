def solution():
    
    shopping_money = 158
    shoes_cost = 45
    bag_cost = shoes_cost - 17
    lunch_cost = bag_cost / 4
    total_spent = shoes_cost + bag_cost + lunch_cost
    remaining_money = shopping_money - total_spent
    result = remaining_money
    return result

print(solution())