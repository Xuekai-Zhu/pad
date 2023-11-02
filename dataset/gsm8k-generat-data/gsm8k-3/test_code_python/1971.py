def solution():
    """Ms. Estrella is an entrepreneur with a startup company having 10 employees. The company makes a revenue of $400000 a month, paying 10% in taxes, 5% of the remaining amount on marketing and ads, 20% of the remaining amount on operational costs, and 15% of the remaining amount on employee wages.  Assuming each employee receives the same wage, calculate the amount of money each employee is paid monthly."""
    # Define the revenue and tax rate
    REVENUE = 400000
    TAX_RATE = 0.1

    # Calculate the amount of taxes paid
    taxes = REVENUE * TAX_RATE

    # Calculate the remaining amount after taxes
    remaining = REVENUE - taxes

    # Calculate the amount spent on marketing and ads
    marketing = remaining * 0.05
    remaining -= marketing

    # Calculate the amount spent on operational costs
    operations = remaining * 0.20
    remaining -= operations

    # Calculate the amount spent on employee wages
    wages = remaining * 0.15

    # Calculate the amount each employee is paid monthly
    employee_pay = wages / 10

    # Display the amount each employee is paid
    result = employee_pay
    return result

print(solution())