def solution():
    visits_per_month = 30000
    days_per_month = 30
    earnings_per_visit = 0.01
    earnings_per_day = visits_per_month / days_per_month * earnings_per_visit
    result = earnings_per_day
    return result

print(solution())