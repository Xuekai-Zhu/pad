def solution():
    
    hourly_rate = 10
    hours_per_day = 10
    days_per_week = 5
    weeks = 4

    
    robby_earnings = hourly_rate * hours_per_day * days_per_week
    jaylen_earnings = hourly_rate * hours_per_day * days_per_week
    miranda_earnings = hourly_rate * hours_per_day * days_per_week

    
    robby_savings = robby_earnings * (2/5)
    jaylen_savings = jaylen_earnings * (3/5)
    miranda_savings = miranda_earnings * 0.5

    
    total_savings = (robby_savings + jaylen_savings + miranda_savings) * weeks

    result = total_savings
    return result

print(solution())