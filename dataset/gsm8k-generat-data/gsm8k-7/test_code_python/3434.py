def solution():
    starting_amount = 500 # grams
    amount_used = 240 # grams
    remaining_amount = starting_amount - amount_used
    spilled_amount = remaining_amount / 2
    remaining_amount = remaining_amount - spilled_amount
    amount_needed = 500 - remaining_amount
    result = amount_needed
    return result

print(solution())