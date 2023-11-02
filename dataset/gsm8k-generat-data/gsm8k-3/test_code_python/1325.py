def solution():
    """Sally earned $1000 at work last month. This month, she received a 10% raise. How much money will she make in total for the two months?"""
    # Define Sally's starting salary and raise percentage
    START_SALARY = 1000
    RAISE_PERCENT = 10

    # Calculate Sally's new salary after the raise
    new_salary = START_SALARY + (START_SALARY * (RAISE_PERCENT/100))

    # Calculate Sally's total earnings over the two months
    total_earnings = START_SALARY + new_salary

    # Display Sally's total earnings
    result = total_earnings
    return result

print(solution())