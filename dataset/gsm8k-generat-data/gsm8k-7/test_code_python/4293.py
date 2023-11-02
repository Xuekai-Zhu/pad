def solution():
    total_cds = 200
    cds_at_10 = 0.4 * total_cds
    cds_at_5 = 0.6 * total_cds

    cds_at_10_bought = cds_at_10 / 2
    cds_at_5_bought = cds_at_5

    cost_at_10 = cds_at_10_bought * 10
    cost_at_5 = cds_at_5_bought * 5

    total_cost = cost_at_10 + cost_at_5
    result = total_cost
    return result

print(solution())