def solution():
    
    visits_per_hour = 50
    hours_per_day = 24
    days_per_month = 30
    dollars_per_visit = 0.1
    total_visits = visits_per_hour * hours_per_day * days_per_month
    dollars_made = total_visits * dollars_per_visit
    result = dollars_made
    return result

print(solution())