def solution():
    
    chess_hours_per_week = 2
    drama_hours_per_week = 8
    glee_hours_per_week = 3
    weeks_per_semester = 12
    sick_weeks = 2
    weeks_before_midterms = 6
    total_hours = (chess_hours_per_week + drama_hours_per_week + glee_hours_per_week) * (weeks_per_semester - sick_weeks - weeks_before_midterms)
    result = total_hours
    return result

print(solution())