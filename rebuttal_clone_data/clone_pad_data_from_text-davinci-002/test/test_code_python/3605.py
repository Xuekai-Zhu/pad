def solution():
    ladders_50 = 10
    ladders_60 = 20
    rungs_50 = 50
    rungs_60 = 60
    cost_per_rung = 2
    total_cost = (ladders_50 * rungs_50 * cost_per_rung) + (ladders_60 * rungs_60 * cost_per_rung)
    result = total_cost
    return result

print(solution())