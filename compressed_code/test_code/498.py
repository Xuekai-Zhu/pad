def solution():
    
    pills_per_day = 2
    pill_cost = 1.5
    insurance_coverage = 0.4
    days_in_month = 30
    pills_per_month = pills_per_day * days_in_month
    unsubsidized_cost_per_month = pills_per_month * pill_cost
    subsidized_cost_per_month = unsubsidized_cost_per_month * (1 - insurance_coverage)
    result = subsidized_cost_per_month
    return result

print(solution())