def solution():
    insurance_cost_per_month = 20
    months_with_insurance = 24
    total_insurance_cost = insurance_cost_per_month * months_with_insurance
    surgery_cost = 5000
    covered_percent = 80
    amount_covered = surgery_cost * (covered_percent / 100)
    total_savings = amount_covered - total_insurance_cost
    result = total_savings
    return result

print(solution())