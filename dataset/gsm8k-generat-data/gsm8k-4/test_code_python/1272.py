def solution():
    """Ruiz receives a monthly salary of $500. If he received a 6% raise, how much will be Ruiz's new salary?"""
    # Define Ruiz's current salary
    current_salary = 500

    # Define the percentage increase
    increase_percent = 6

    # Calculate the increase in salary
    increase = current_salary * (increase_percent / 100)

    # Calculate Ruiz's new salary
    new_salary = current_salary + increase

    result = new_salary
    return result

print(solution())