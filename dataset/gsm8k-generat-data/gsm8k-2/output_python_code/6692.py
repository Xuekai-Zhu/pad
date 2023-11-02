def solution():
    """John's hair grows 1.5 inches every month. Every time it gets to 9 inches long he cuts it down to 6 inches. A haircut costs $45 and he gives a 20% tip. How much does he spend on haircuts a year?"""
    # Calculate how many haircuts John gets in a year
    inches_before_cut = 9
    inches_after_cut = 6
    inches_cut_per_cycle = inches_before_cut - inches_after_cut
    cycles_per_year = 12 / (inches_cut_per_cycle / 1.5)

    # Calculate the cost of each haircut
    haircut_cost = 45
    tip_percent = 0.2
    tip_amount = haircut_cost * tip_percent
    total_cost_per_haircut = haircut_cost + tip_amount

    # Calculate the total cost of haircuts in a year
    total_cost = total_cost_per_haircut * cycles_per_year
    result = total_cost
    return result

print(solution())