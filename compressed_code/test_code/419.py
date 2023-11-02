def solution():
    
    target_income = 100
    daily_income = 0
    monday_harvest = 8
    tuesday_harvest = monday_harvest * 3
    wednesday_harvest = 0
    total_harvest = monday_harvest + tuesday_harvest + wednesday_harvest
    total_income = total_harvest * 2
    remaining_income = target_income - total_income
    pounds_needed_on_thursday = remaining_income / 2
    result = pounds_needed_on_thursday
    return result

print(solution())