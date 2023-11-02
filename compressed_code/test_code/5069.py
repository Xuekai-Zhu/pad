def solution():
    
    total_paid = 146
    flat_rate = 20
    per_minute_rate = 7
    minutes_tutored = (total_paid - flat_rate) / per_minute_rate
    result = minutes_tutored
    return result

print(solution())