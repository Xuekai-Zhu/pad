def solution():
    
    starting_amount = 10000 
    morning_cooked = 9/10 * starting_amount
    remaining_rice = starting_amount - morning_cooked
    evening_cooked = 1/4 * remaining_rice
    amount_left = remaining_rice - evening_cooked
    result = amount_left
    return result

print(solution())