def solution():
    """Hansel makes $30,000 a year and just received a 10% raise.  Gretel makes the same amount as Hansel but received a 15% raise.  How much more money will Gretel make compared to Hansel?"""
    # Define Hansel's salary and raise
    HANSEL_SALARY = 30000
    HANSEL_RAISE = 0.10

    # Calculate Hansel's new salary
    hansel_new_salary = HANSEL_SALARY * (1 + HANSEL_RAISE)

    # Define Gretel's salary and raise
    GRETEL_SALARY = HANSEL_SALARY
    GRETEL_RAISE = 0.15

    # Calculate Gretel's new salary
    gretel_new_salary = GRETEL_SALARY * (1 + GRETEL_RAISE)

    # Calculate the difference between Gretel's and Hansel's salaries
    difference = gretel_new_salary - hansel_new_salary

    # Display the difference
    result = difference
    return result

print(solution())