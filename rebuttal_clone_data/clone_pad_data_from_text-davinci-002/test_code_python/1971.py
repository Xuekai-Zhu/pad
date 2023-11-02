def solution():
    revenue = 400000
    taxes = revenue * 0.1
    marketing_and_ads = (revenue - taxes) * 0.05
    operational_costs = (revenue - taxes - marketing_and_ads) * 0.2
    employee_wages = (revenue - taxes - marketing_and_ads - operational_costs) * 0.15
    result = employee_wages / 10
    return result

print(solution())