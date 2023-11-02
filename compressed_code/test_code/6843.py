def solution():
    
    old_wage = 16
    old_hours = 25
    new_wage = 20
    new_hours = 40
    weeks_per_year = 52
    old_salary = old_wage * old_hours * weeks_per_year
    new_salary = new_wage * new_hours * weeks_per_year
    difference = new_salary - old_salary
    result = difference
    return result

print(solution())