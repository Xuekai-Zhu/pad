def solution():
    """A secretary who has been working for 6 years and who earns €10,000 a month has obtained a salary increase of 2%. What is her new salary?"""
    # Define the initial salary and the percentage increase
    initial_salary = 10000
    percentage_increase = 0.02

    # Calculate the new salary
    new_salary = initial_salary * (1 + percentage_increase)

    # Return the result
    result = new_salary
    return result

print(solution())