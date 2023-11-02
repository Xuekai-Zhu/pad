def solution():
    
    last_year_pay = 100000
    last_year_bonus = 10000
    bonus_percentage = last_year_bonus / last_year_pay
    this_year_pay = 200000
    this_year_bonus = this_year_pay * bonus_percentage
    total_pay = this_year_pay + this_year_bonus
    result = total_pay
    return result

print(solution())