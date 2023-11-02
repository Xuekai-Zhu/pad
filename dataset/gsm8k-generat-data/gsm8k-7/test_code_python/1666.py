def solution():
    cost_per_pack = 0.5
    num_days_per_week = 5
    num_weeks = 4

    # Calculate the total number of packs of chips that Calvin buys
    total_packs = num_days_per_week * num_weeks

    # Calculate the total cost of all packs of chips that Calvin buys
    total_cost = total_packs * cost_per_pack
    result = total_cost
    return result

print(solution())