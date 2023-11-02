def solution():
    
    initial_amount = 2000
    furniture_cost = 400
    remaining_amount = initial_amount - furniture_cost
    amount_given = remaining_amount * 3/4
    amount_left = remaining_amount - amount_given
    result = amount_left
    return result

print(solution())