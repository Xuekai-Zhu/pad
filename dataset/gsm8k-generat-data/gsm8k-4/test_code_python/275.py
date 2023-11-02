def solution():
    """Hansel makes $30,000 a year and just received a 10% raise. Gretel makes the same amount as Hansel but received a 15% raise. How much more money will Gretel make compared to Hansel?"""
    # Define the initial salary and the percentage raise for Hansel and Gretel
    hansel_salary = 30000
    hansel_raise = 0.1
    gretel_salary = 30000
    gretel_raise = 0.15

    # Calculate the new salaries for Hansel and Gretel
    hansel_new_salary = hansel_salary * (1 + hansel_raise)
    gretel_new_salary = gretel_salary * (1 + gretel_raise)

    # Calculate the difference in salary between Hansel and Gretel
    salary_difference = gretel_new_salary - hansel_new_salary

    # Display the result
    result = salary_difference
    return result

print(solution())