def solution():
    initial_height = 2
    growth_rate = 0.5
    cutting_height = 4
    cost_per_cut = 100

    # Calculate the number of cuts needed per year
    months_per_year = 12
    growth_per_month = growth_rate * months_per_year
    growth_to_cut = cutting_height - initial_height
    cuts_per_year = growth_to_cut / growth_per_month

    # Calculate the cost per year
    cost_per_year = cuts_per_year * cost_per_cut
    result = cost_per_year
    return result

print(solution())