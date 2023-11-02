def solution():
    hansel_salary = 30000  # Hansel makes $30,000 a year
    gretel_salary = hansel_salary  # Gretel makes the same amount as Hansel
    hansel_raise = 0.1  # Hansel received a 10% raise
    gretel_raise = 0.15  # Gretel received a 15% raise

    # Calculate the new salary for Hansel after the raise
    hansel_new_salary = hansel_salary * (1 + hansel_raise)

    # Calculate the new salary for Gretel after the raise
    gretel_new_salary = gretel_salary * (1 + gretel_raise)

    # Calculate the difference in salary between Gretel and Hansel
    salary_difference = gretel_new_salary - hansel_new_salary
    result = salary_difference
    return result

print(solution())