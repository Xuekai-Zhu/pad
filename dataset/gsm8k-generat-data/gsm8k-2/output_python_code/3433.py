def solution():
    """Lucy had a 500g bag of flour but used 240g and spilled half of what was left. How much flour does she need to buy to have a full bag of flour in the cupboard?"""
    starting_amount = 500
    used_amount = 240
    remaining_amount = starting_amount - used_amount
    spilled_amount = remaining_amount / 2
    total_amount = starting_amount - used_amount - spilled_amount
    amount_to_buy = starting_amount - total_amount
    result = amount_to_buy
    return result

print(solution())