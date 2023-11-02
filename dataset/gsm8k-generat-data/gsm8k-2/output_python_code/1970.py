def solution():
    """Ms. Estrella is an entrepreneur with a startup company having 10 employees. The company makes a revenue of $400000 a month, paying 10% in taxes, 5% of the remaining amount on marketing and ads, 20% of the remaining amount on operational costs, and 15% of the remaining amount on employee wages. Assuming each employee receives the same wage, calculate the amount of money each employee is paid monthly."""
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