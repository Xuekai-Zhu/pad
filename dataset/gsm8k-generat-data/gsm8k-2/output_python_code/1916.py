def solution():
    """A secretary who has been working for 6 years and who earns €10,000 a month has obtained a salary increase of 2%. What is her new salary?"""
    current_salary = 10000
    years_worked = 6
    salary_increase_percent = 2
    new_salary = current_salary * ((100 + salary_increase_percent) / 100)
    result = new_salary
    return result

print(solution())