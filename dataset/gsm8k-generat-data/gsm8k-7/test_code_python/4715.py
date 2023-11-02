def solution():
    num_weeks = 4
    trash_bins = 2
    recycling_bins = 1
    trash_cost_per_week = 10 * trash_bins
    recycling_cost_per_week = 5 * recycling_bins
    total_cost_per_week = trash_cost_per_week + recycling_cost_per_week
    discounted_cost_per_week = total_cost_per_week - (total_cost_per_week * 0.18)
    fine = 20
    total_cost = discounted_cost_per_week * num_weeks + fine
    result = total_cost
    return result

print(solution())