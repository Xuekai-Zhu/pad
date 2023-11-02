def solution():
    ticket_cost = 1000000
    decadel_reduction = 10
    cost_reduction_rate = 50
    mattys_age = 30
    decades_since_birth = mattys_age / decadel_reduction
    total_reduction = decades_since_birth * cost_reduction_rate
    cost_after_reduction = ticket_cost - total_reduction
    result = cost_after_reduction
    return result

print(solution())