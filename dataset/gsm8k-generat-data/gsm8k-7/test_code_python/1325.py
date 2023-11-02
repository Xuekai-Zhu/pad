def solution():
    initial_salary = 1000
    raise_percentage = 0.10  # 10% raise

    # Calculate the amount of raise Sally received
    raise_amount = initial_salary * raise_percentage

    # Calculate Sally's new salary after the raise
    new_salary = initial_salary + raise_amount

    # Calculate Sally's total earnings for two months
    total_earnings = initial_salary + new_salary
    result = total_earnings
    return result

print(solution())