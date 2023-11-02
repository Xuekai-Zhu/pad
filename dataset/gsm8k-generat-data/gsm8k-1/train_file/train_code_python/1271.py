def solution():
    """Ruiz receives a monthly salary of $500. If he received a 6% raise, how much will be Ruiz's new salary?"""
    current_salary = 500
    raise_percent = 6
    raise_amount = current_salary * (raise_percent / 100)
    new_salary = current_salary + raise_amount
    result = new_salary
    return result

print(solution())