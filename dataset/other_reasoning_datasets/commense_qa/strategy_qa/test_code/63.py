def solution():
    butler_salary = 60000
    middle_class_income_range = range(48000, 145000)
    if butler_salary in middle_class_income_range:
        result = "maybe"
    else:
        result = "no"
    return result

print(solution())