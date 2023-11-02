def solution():
    hansel_salary = 30000
    hansel_raise = hansel_salary * 0.1
    hansel_total_salary = hansel_salary + hansel_raise

    gretel_salary = 30000
    gretel_raise = gretel_salary * 0.15
    gretel_total_salary = gretel_salary + gretel_raise

    difference = gretel_total_salary - hansel_total_salary
    result = difference
    return result

print(solution())