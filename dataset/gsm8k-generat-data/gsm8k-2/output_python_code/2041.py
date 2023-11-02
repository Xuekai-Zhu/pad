def solution():
    """The PTA had saved $400 set aside after a fundraising event. They spent a fourth of the money on school supplies. Then they spent half of what was left on food for the faculty. How much money did they have left?"""
    starting_amount = 400
    supplies_cost = starting_amount / 4
    remaining_amount = starting_amount - supplies_cost
    food_cost = remaining_amount / 2
    amount_left = remaining_amount - food_cost
    result = amount_left
    return result

print(solution())