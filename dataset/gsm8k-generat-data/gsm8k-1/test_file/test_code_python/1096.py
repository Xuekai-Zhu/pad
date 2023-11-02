def solution():
    """Bobby takes a 30 min lunch and 2 15 minutes break per day at the office. After 5 days, how many hours do his lunches and breaks add up to?"""
    lunch_time = 0.5
    break_time = 0.25
    days_worked = 5
    total_time = (lunch_time + (break_time * 2)) * days_worked
    result = total_time
    
    return result

print(solution())