def solution():
    # Calculate the amount of money paid in taxes
    taxes = 0.1 * 400000

    # Calculate the remaining amount after paying taxes
    remaining_amount = 400000 - taxes

    # Calculate the amount of money spent on marketing and ads
    marketing = 0.05 * remaining_amount

    # Calculate the remaining amount after paying for marketing and ads
    remaining_amount -= marketing

    # Calculate the amount of money spent on operational costs
    operational_costs = 0.2 * remaining_amount

    # Calculate the remaining amount after paying for operational costs
    remaining_amount -= operational_costs

    # Calculate the amount of money spent on employee wages
    wages = 0.15 * remaining_amount

    # Calculate the amount of money each employee is paid monthly
    employee_wages = wages / 10

    result = employee_wages
    return result

print(solution())