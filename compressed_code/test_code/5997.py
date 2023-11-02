def solution():
    
    hansel_salary = 30000
    hansel_raise = 0.1
    gretel_salary = 30000
    gretel_raise = 0.15
    
    hansel_new_salary = hansel_salary + (hansel_salary * hansel_raise)
    gretel_new_salary = gretel_salary + (gretel_salary * gretel_raise)
    
    difference = gretel_new_salary - hansel_new_salary
    result = difference
    
    return result

print(solution())