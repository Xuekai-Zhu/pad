def solution():
    initial_salary = 600  # The company pays each of its employees $600 in a month
    increased_salary = initial_salary * 0.1  # The company increases the salaries of each of its employees by 10% of the initial salary every year
    years_clocked = 5  # Sylvie clocked 5 years

    # Calculate Sylvie's annual salary after three more years of service
    annual_salary = (increased_salary * years_clocked) + (increased_salary * years_clocked) + (increased_salary * 3)
    result = annual_salary
    return result

print(solution())