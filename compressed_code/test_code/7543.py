def solution():
    
    insurance_cost_per_month = 80
    percent_cost_to_pay = 40
    cost_to_pay_per_month = insurance_cost_per_month * (percent_cost_to_pay / 100)
    cost_to_pay_per_year = cost_to_pay_per_month * 12
    result = cost_to_pay_per_year
    return result

print(solution())