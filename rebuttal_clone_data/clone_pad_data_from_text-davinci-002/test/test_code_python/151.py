def solution():
    
    hansel_salary = 30000
    hansel_raise = 10
    gretel_salary = hansel_salary
    gretel_raise = 15
    hansel_new_salary = hansel_salary + (hansel_salary * (hansel_raise / 100))
    gretel_new_salary = gretel_salary + (gretel_salary * (gretel_raise / 100))
    salary_difference = gretel_new_salary - hansel_new_salary
    result = salary_difference
    return result

print(solution())