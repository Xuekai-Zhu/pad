def solution():
    MSRP = 30
    insurance_plan = MSRP * 0.2
    state_tax = (insurance_plan + MSRP) * 0.5
    total_cost = insurance_plan + state_tax + MSRP
    result = total_cost
    return result

print(solution())