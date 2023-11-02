def solution():
    num_employees = 10
    revenue = 400000
    tax_rate = 0.1
    marketing_rate = 0.05
    operational_rate = 0.2
    wage_rate = 0.15

    # Calculate the amount paid in taxes
    taxes = revenue * tax_rate

    # Calculate the remaining amount after taxes
    after_tax = revenue - taxes

    # Calculate the amount spent on marketing and ads
    marketing = after_tax * marketing_rate

    # Calculate the remaining amount after marketing
    after_marketing = after_tax - marketing

    # Calculate the amount spent on operational costs
    operational_costs = after_marketing * operational_rate

    # Calculate the remaining amount after operational costs
    after_operational = after_marketing - operational_costs

    # Calculate the amount spent on employee wages
    wage_amount = after_operational * wage_rate

    # Calculate the amount paid to each employee
    wage_per_employee = wage_amount / num_employees

    result = wage_per_employee
    return result

print(solution())