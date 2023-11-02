def solution():
    """Lulu has $65 in her piggy bank. She spent $5 on ice cream. She then spent half of the remainder of the money on a t-shirt. Afterwards, she went to the bank and deposited a fifth of her remaining money. How much cash was Lulu left with?"""
    starting_money = 65
    ice_cream_cost = 5
    money_remaining_after_ice_cream = starting_money - ice_cream_cost
    t_shirt_cost = money_remaining_after_ice_cream / 2
    money_remaining_after_t_shirt = money_remaining_after_ice_cream - t_shirt_cost
    money_deposited = money_remaining_after_t_shirt / 5
    money_left = money_remaining_after_t_shirt - money_deposited
    result = money_left
    return result

print(solution())