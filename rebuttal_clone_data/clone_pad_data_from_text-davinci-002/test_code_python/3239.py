def solution():
    total_cost = 40000 + 70000
    insurance_coverage = 0.8
    amount_paid_by_insurance = total_cost * insurance_coverage
    carl_owes = total_cost - amount_paid_by_insurance
    result = carl_owes
    return result

print(solution())