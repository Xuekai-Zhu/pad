def solution():
    """Ruiz receives a monthly salary of $500. If he received a 6% raise, how much will be Ruiz's new salary?"""
    current_salary = 500
    raise_percent = 0.06
    new_salary = current_salary + (current_salary * raise_percent)
    result = new_salary
    return result

print(solution())