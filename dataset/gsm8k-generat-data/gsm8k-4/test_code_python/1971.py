def solution():
    """Ms. Estrella is an entrepreneur with a startup company having 10 employees. The company makes a revenue of $400000 a month, paying 10% in taxes, 5% of the remaining amount on marketing and ads, 20% of the remaining amount on operational costs, and 15% of the remaining amount on employee wages. Assuming each employee receives the same wage, calculate the amount of money each employee is paid monthly."""
    # Define the revenue of the company and the percentage of taxes paid
    revenue = 400000
    taxes = 0.1

    # Calculate the amount of taxes paid
    taxes_paid = revenue * taxes

    # Calculate the remaining revenue after paying taxes
    remaining_revenue = revenue - taxes_paid

    # Calculate the amount spent on marketing and ads
    marketing_costs = remaining_revenue * 0.05

    # Calculate the remaining revenue after marketing costs
    remaining_revenue -= marketing_costs

    # Calculate the amount spent on operational costs
    operational_costs = remaining_revenue * 0.2

    # Calculate the remaining revenue after operational costs
    remaining_revenue -= operational_costs

    # Calculate the amount spent on employee wages
    wages = remaining_revenue * 0.15

    # Calculate the amount of money each employee is paid monthly
    employee_payment = wages / 10

    result = employee_payment
    return result

print(solution())