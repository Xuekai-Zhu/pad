def solution():
    """Lulu has $65 in her piggy bank. She spent $5 on ice cream. She then spent half of the remainder of the money on a t-shirt. Afterwards, she went to the bank and deposited a fifth of her remaining money. How much cash was Lulu left with?"""
    starting_amount = 65
    ice_cream_cost = 5
    tshirt_cost = (starting_amount - ice_cream_cost) / 2
    remaining_amount = starting_amount - ice_cream_cost - tshirt_cost
    deposit_amount = remaining_amount / 5
    final_amount = remaining_amount - deposit_amount
    result = final_amount
    return result

print(solution())