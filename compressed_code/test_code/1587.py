def solution():
    
    starting_amount = 400
    supplies_cost = starting_amount / 4
    remaining_amount = starting_amount - supplies_cost
    food_cost = remaining_amount / 2
    amount_left = remaining_amount - food_cost
    result = amount_left
    return result

print(solution())