def solution():
    last_year_salary = 100000
    last_year_bonus_percentage = 10
    this_year_salary = 200000
    this_year_bonus_percentage = this_year_salary * (last_year_bonus_percentage / 100)
    total_pay = this_year_salary + this_year_bonus_percentage
    result = total_pay
    return result

print(solution())