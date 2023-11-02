def solution():
    hansel_salary = 30000
    hansel_raise = 0.1  # 10% raise
    gretel_raise = 0.15  # 15% raise

    # Calculate Hansel's new salary after the raise
    hansel_new_salary = hansel_salary * (1 + hansel_raise)

    # Calculate Gretel's new salary after the raise
    gretel_new_salary = hansel_salary * (1 + gretel_raise)

    # Calculate the difference in their new salaries
    salary_difference = gretel_new_salary - hansel_new_salary

    result = salary_difference
    return result

print(solution())