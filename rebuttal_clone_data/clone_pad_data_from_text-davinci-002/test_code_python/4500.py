def solution():
    initial_amount = 1000
    amount_to_change = initial_amount * (3/10)
    changed_amount = amount_to_change - (amount_to_change % 50)
    leftover_amount = initial_amount - changed_amount
    total_amount= changed_amount + leftover_amount
    result = total_amount
    
    return result

print(solution())