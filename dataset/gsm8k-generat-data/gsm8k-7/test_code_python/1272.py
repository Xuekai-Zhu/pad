def solution():
    current_salary = 500
    raise_percentage = 0.06  # 6% raise

    # Calculate the amount of the raise
    raise_amount = current_salary * raise_percentage

    # Calculate the new salary after the raise
    new_salary = current_salary + raise_amount
    result = new_salary
    return result

print(solution())