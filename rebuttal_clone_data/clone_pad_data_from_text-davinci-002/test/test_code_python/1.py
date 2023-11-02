def solution():
    
    hourly_rate = 12
    minutes_worked = 50
    hourly_equivalent = minutes_worked / 60
    total_earned = hourly_rate * hourly_equivalent
    result = total_earned
    return result

print(solution())