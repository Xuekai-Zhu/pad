def solution():
    """Ruiz receives a monthly salary of $500. If he received a 6% raise, how much will be Ruiz's new salary?"""
    # Define Ruiz's salary and the percentage raise
    salary = 500
    percentage_raise = 6

    # Calculate the amount of the raise
    raise_amount = salary * (percentage_raise / 100)

    # Calculate Ruiz's new salary
    new_salary = salary + raise_amount

    # Display Ruiz's new salary
    result = new_salary
    return result

print(solution())