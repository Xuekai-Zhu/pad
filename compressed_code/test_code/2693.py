def solution():
    
    bread_cost = 5
    orange_juice_cost = 2
    bread_count = 5
    orange_juice_count = 4
    total_spent = (bread_cost * bread_count) + (orange_juice_cost * orange_juice_count)
    money_left = 74 - total_spent
    result = money_left
    return result

print(solution())