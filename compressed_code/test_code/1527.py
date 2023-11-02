def solution():
    
    revenue = 400000
    tax = revenue * 0.1
    remaining1 = revenue - tax
    marketing = remaining1 * 0.05
    remaining2 = remaining1 - marketing
    operational_costs = remaining2 * 0.2
    remaining3 = remaining2 - operational_costs
    employee_wages = remaining3 * 0.15
    total_wages = employee_wages / 10
    result = total_wages
    return result

print(solution())