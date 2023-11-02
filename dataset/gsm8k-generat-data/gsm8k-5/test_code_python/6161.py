def solution():
    total_salary = 90  # The total salary of the three people is $90
    terrence_salary = 30  # Terrence earns $30
    jermaine_salary = terrence_salary + 5  # Jermaine earns $5 more than Terrence
    emilee_salary = total_salary - terrence_salary - jermaine_salary  # Emilee's salary is the difference of the total salary and the sum of the salaries of Terrence and Jermaine
    result = emilee_salary
    return result

print(solution())