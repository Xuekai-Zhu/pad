def solution():
    
    teacher_rate = 20
    coach_rate = 30
    teacher_hours_per_week = 35
    coach_hours_per_week = 15
    weeks_per_year = 50
    teacher_salary = teacher_rate * teacher_hours_per_week * weeks_per_year
    coach_salary = coach_rate * coach_hours_per_week * weeks_per_year
    annual_salary = teacher_salary + coach_salary
    result = annual_salary
    return result

print(solution())