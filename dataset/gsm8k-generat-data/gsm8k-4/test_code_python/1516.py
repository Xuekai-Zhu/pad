def solution():
    """Lucille has to divide the revenue from her business in the ratio of 4:11 for employee salaries and stock purchases, respectively. If she has $3000 as her revenue, calculate the total amount of money she spends on employee salary?"""
    # Define the total revenue and the salary-to-purchases ratio
    total_revenue = 3000
    salary_purchases_ratio = 4/11

    # Calculate the total amount spent on employee salaries
    salary_total = total_revenue * salary_purchases_ratio

    result = salary_total
    return result

print(solution())