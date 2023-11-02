def solution():
    
    hansel_salary = 30000
    hansel_raise = 0.1
    hansel_new_salary = hansel_salary * (1 + hansel_raise)
    gretel_raise = 0.15
    gretel_new_salary = hansel_salary * (1 + gretel_raise)
    difference = gretel_new_salary - hansel_new_salary
    result = difference
    return result

print(solution())