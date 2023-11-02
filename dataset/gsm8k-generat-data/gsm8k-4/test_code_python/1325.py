def solution():
    """Sally earned $1000 at work last month. This month, she received a 10% raise. How much money will she make in total for the two months?"""
    # Define the initial amount Sally earned
    initial_salary = 1000

    # Calculate Sally's new salary after the raise
    new_salary = initial_salary * 1.1

    # Calculate Sally's total earnings for two months
    total_earnings = initial_salary + new_salary

    # return the result
    result = total_earnings
    return result

print(solution())