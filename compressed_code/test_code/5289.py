def solution():
    
    starting_amount = 80
    monday_spent = starting_amount / 2
    tuesday_left = starting_amount - monday_spent
    tuesday_spent = tuesday_left / 5
    wednesday_left = tuesday_left - tuesday_spent
    wednesday_spent = wednesday_left * 3 / 8
    remaining_amount = wednesday_left - wednesday_spent
    result = remaining_amount
    return result

print(solution())