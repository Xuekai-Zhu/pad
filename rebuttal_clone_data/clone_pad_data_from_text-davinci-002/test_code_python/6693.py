def solution():
    # length_growth is in inches
    length_growth = 1.5
    # length_cut is in inches
    length_cut = 9
    # length_after_cut is in inches
    length_after_cut = 6
    # tip_percent is in percent
    tip_percent = 20
    # haircut_cost is in dollars
    haircut_cost = 45
    # length_remaining is in inches
    length_remaining = length_cut - length_after_cut
    # num_haircuts is a whole number
    num_haircuts = 12 / length_growth
    # tip_amount is in dollars
    tip_amount = haircut_cost * (tip_percent / 100)
    # total_cost is in dollars
    total_cost = num_haircuts * (haircut_cost + tip_amount)
    result = total_cost
    return result

print(solution())