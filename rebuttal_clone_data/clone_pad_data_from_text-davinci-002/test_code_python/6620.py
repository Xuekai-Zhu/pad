def solution():
    hours_worked_per_week = 10
    days_worked_per_week = 5
    salary_per_hour = 10
    robby_percent_saved = 2/5
    jaylen_percent_saved = 3/5
    miranda_percent_saved = 1/2
    robby_savings = (hours_worked_per_week * days_worked_per_week * salary_per_hour) * robby_percent_saved
    jaylen_savings = (hours_worked_per_week * days_worked_per_week * salary_per_hour) * jaylen_percent_saved
    miranda_savings = (hours_worked_per_week * days_worked_per_week * salary_per_hour) * miranda_percent_saved
    total_savings = robby_savings + jaylen_savings + miranda_savings
    result = total_savings
    
    return result

print(solution())