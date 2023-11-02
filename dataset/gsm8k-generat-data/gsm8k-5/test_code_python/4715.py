def solution():
    num_weeks = 4  # Mary is paying for a month with exactly 4 weeks
    trash_bins = 2  # Mary has 2 trash bins
    recycling_bins = 1  # Mary has 1 recycling bin
    trash_cost_per_week = 10 * trash_bins  # The cost of trash bins per week
    recycling_cost_per_week = 5 * recycling_bins  # The cost of recycling bins per week
    total_cost_per_week = trash_cost_per_week + recycling_cost_per_week  # The total cost per week
    total_cost = num_weeks * total_cost_per_week  # The total cost for the month

    # Calculate the discount Mary gets for being elderly
    elderly_discount = 0.18 * total_cost
    discounted_total_cost = total_cost - elderly_discount

    # Add the fine for inappropriately using the recycling bin
    final_total_cost = discounted_total_cost + 20
    result = final_total_cost
    return result

print(solution())