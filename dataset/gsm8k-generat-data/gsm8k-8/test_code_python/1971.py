def solution():
    # Calculate the amount of taxes paid
    taxes = 0.1 * 400000

    # Calculate the remaining revenue after paying taxes
    revenue_after_taxes = 400000 - taxes

    # Calculate the amount spent on marketing and ads
    marketing_ads = 0.05 * revenue_after_taxes

    # Calculate the remaining revenue after marketing and ads
    revenue_after_marketing_ads = revenue_after_taxes - marketing_ads

    # Calculate the amount spent on operational costs
    operational_costs = 0.2 * revenue_after_marketing_ads

    # Calculate the remaining revenue after operational costs
    revenue_after_operational_costs = revenue_after_marketing_ads - operational_costs

    # Calculate the amount spent on employee wages
    employee_wages = 0.15 * revenue_after_operational_costs

    # Calculate the amount each employee is paid monthly
    employee_salary = employee_wages / 10
    result = employee_salary
    return result

print(solution())