def solution():
    current_salary = 10000  # The secretary currently earns €10,000 per month
    years_worked = 6  # The secretary has been working for 6 years
    salary_increase = 0.02  # The salary increase is 2%

    # Calculate the multiplier for the salary increase based on the number of years worked
    if years_worked < 5:
        multiplier = 1
    elif years_worked < 10:
        multiplier = 1.05
    else:
        multiplier = 1.10

    # Calculate the new salary with the salary increase and years worked multiplier
    new_salary = current_salary * (1 + salary_increase) * multiplier
    result = new_salary
    return result

print(solution())