def solution():
    """Mrs. Snyder used to spend 40% of her monthly income on rent and utilities. Her salary was recently increased by $600 so now her rent and utilities only amount to 25% of her monthly income. How much was her previous monthly income?"""
    # Define the initial percentage spent on rent and utilities and the final percentage
    INITIAL_PERCENTAGE = 0.4
    FINAL_PERCENTAGE = 0.25

    # Define the increase in salary
    salary_increase = 600

    # Calculate the initial amount spent on rent and utilities
    initial_rent_utilities = INITIAL_PERCENTAGE * x

    # Calculate the final amount spent on rent and utilities
    final_rent_utilities = FINAL_PERCENTAGE * (x + salary_increase)

    # Solve for the initial monthly income
    x = (final_rent_utilities - salary_increase) / (FINAL_PERCENTAGE - INITIAL_PERCENTAGE)

    # Return the result
    result = x
    return result

print(solution())