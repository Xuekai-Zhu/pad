def solution():
    # Calculate the amount of money left after taxes are paid
    revenue = 400000
    tax = 0.1
    remaining_after_tax = revenue * (1 - tax)

    # Calculate the amount of money spent on marketing and ads
    marketing = 0.05
    remaining_after_marketing = remaining_after_tax * (1 - marketing)

    # Calculate the amount of money spent on operational costs
    operational_costs = 0.2
    remaining_after_operational_costs = remaining_after_marketing * (1 - operational_costs)

    # Calculate the amount of money spent on employee wages
    wages = 0.15
    remaining_after_wages = remaining_after_operational_costs * (1 - wages)
    amount_per_employee = remaining_after_wages / 10

    result = amount_per_employee
    return result

print(solution())