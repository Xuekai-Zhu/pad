def solution():
    """Lucille has to divide the revenue from her business in the ratio of 4:11 for employee salaries and stock purchases, respectively. If she has $3000 as her revenue, calculate the total amount of money she spends on employee salary?"""
    # Define the ratio of revenue spent on employee salaries to stock purchases
    SALARY_RATIO = 4
    STOCK_RATIO = 11

    # Define the total revenue
    total_revenue = 3000

    # Calculate the amount spent on employee salaries
    salary_amount = (SALARY_RATIO / (SALARY_RATIO + STOCK_RATIO)) * total_revenue

    # Display the amount spent on employee salaries
    result = salary_amount
    return result

print(solution())