def solution():
    
    pills_per_day = 2
    cost_per_pill = 1.5
    days_per_month = 30
    insurance_coverage = 0.4
    total_pills = pills_per_day * days_per_month
    cost_before_coverage = total_pills * cost_per_pill
    covered_cost = cost_before_coverage * insurance_coverage
    out_of_pocket_cost = cost_before_coverage - covered_cost
    result = out_of_pocket_cost
    return result

print(solution())