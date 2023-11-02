def solution():
    """The PTA had saved $400 set aside after a fundraising event. They spent a fourth of the money on school supplies. Then they spent half of what was left on food for the faculty. How much money did they have left?"""
    starting_money = 400
    school_supplies = starting_money / 4
    remaining_money = starting_money - school_supplies
    food_cost = remaining_money / 2
    final_amount = remaining_money - food_cost
    result = final_amount
    return result

print(solution())