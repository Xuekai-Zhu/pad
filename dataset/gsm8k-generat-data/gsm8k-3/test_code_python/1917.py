def solution():
    """A secretary who has been working for 6 years and who earns €10,000 a month has obtained a salary increase of 2%. What is her new salary?"""
    # Define the current salary and the percentage increase
    current_salary = 10000
    increase_percent = 2

    # Calculate the increase amount and the new salary
    increase_amount = current_salary * increase_percent / 100
    new_salary = current_salary + increase_amount

    # Display the new salary
    result = new_salary
    return result

print(solution())