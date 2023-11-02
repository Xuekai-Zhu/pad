def solution():
    # Calculate the number of months it takes for the grass to grow back to 4 inches
    growth_per_month = 0.5  # The grass grows 0.5 inches per month
    initial_height = 2  # John initially cuts the grass to 2 inches
    final_height = 4  # John cuts the grass back down to 2 inches when it reaches 4 inches
    months = (final_height - initial_height) / growth_per_month

    # Calculate the cost per month of cutting the grass
    cost_per_cut = 100  # It costs $100 to get the grass cut
    cuts_per_year = 12 / months  # John needs to get his grass cut this many times per year
    cost_per_month = cost_per_cut / cuts_per_year

    # Calculate the cost per year of cutting the grass
    cost_per_year = cost_per_month * 12
    result = cost_per_year
    return result

print(solution())