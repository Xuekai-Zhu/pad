def solution():
    
    employees = 10
    revenue = 400000
    taxes = revenue * 0.1
    remaining_amount = revenue - taxes
    marketing = remaining_amount * 0.05
    remaining_amount -= marketing
    operational_costs = remaining_amount * 0.2
    remaining_amount -= operational_costs
    wage_budget = remaining_amount * 0.15
    wage_per_employee = wage_budget / employees
    result = wage_per_employee
    return result

print(solution())