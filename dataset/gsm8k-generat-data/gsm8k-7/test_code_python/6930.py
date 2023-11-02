def solution():
    starting_amount = 9.0
    drink_cost = 1.75
    other_cost = 1.25
    
    # Calculate the total amount spent
    total_spent = drink_cost + other_cost
    
    # Calculate the remaining balance
    remaining_balance = starting_amount - total_spent
    result = remaining_balance
    return result

print(solution())