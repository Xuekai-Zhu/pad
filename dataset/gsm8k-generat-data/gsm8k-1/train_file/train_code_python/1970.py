def solution():
    """Ms. Estrella is an entrepreneur with a startup company having 10 employees. The company makes a revenue of $400000 a month, paying 10% in taxes, 5% of the remaining amount on marketing and ads,
    20% of the remaining amount on operational costs, and 15% of the remaining amount on employee wages. Assuming each employee receives the same wage, calculate the amount of money each employee is paid monthly."""
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