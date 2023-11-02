def solution():
    
    starting_amount = 500
    used_amount = 240
    remaining_amount = starting_amount - used_amount
    spilled_amount = remaining_amount / 2
    total_amount = starting_amount - used_amount - spilled_amount
    amount_to_buy = starting_amount - total_amount
    result = amount_to_buy
    return result

print(solution())