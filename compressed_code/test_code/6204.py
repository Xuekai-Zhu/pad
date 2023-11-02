def solution():
    
    initial_amount = 3000
    additional_amount = 200
    amount_given = 1200
    
    total_amount = initial_amount + additional_amount
    remaining_amount = total_amount - amount_given
    
    result = remaining_amount
    return result

print(solution())