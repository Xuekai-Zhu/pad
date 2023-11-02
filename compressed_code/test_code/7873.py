def solution():
    
    initial_amount = 75
    ticket_cost = 30
    food_cost = 13
    shirt_cost = 23
    total_spent = ticket_cost + food_cost + shirt_cost
    money_left = initial_amount - total_spent
    result = money_left
    return result

print(solution())