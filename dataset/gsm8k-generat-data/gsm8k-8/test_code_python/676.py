def solution():
    pills_per_day = 2
    cost_per_pill = 1.5
    days_in_month = 30

    total_cost = pills_per_day * cost_per_pill * days_in_month
    insurance_coverage = 0.4 * total_cost
    out_of_pocket_cost = total_cost - insurance_coverage

    result = out_of_pocket_cost
    return result

print(solution())