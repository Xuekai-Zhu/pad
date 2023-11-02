def solution():
    hats_per_day = 1
    days_per_week = 7
    weeks = 2
    total_hats = hats_per_day * days_per_week * weeks
    cost_per_hat = 50
    total_cost = cost_per_hat * total_hats
    result = total_cost
    return result

print(solution())