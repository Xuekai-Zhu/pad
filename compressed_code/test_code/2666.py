def solution():
    
    laps = 24
    distance = laps * 100
    time = 12
    earnings = (distance / 100) * 3.5
    earnings_per_minute = earnings / time
    result = earnings_per_minute
    return result

print(solution())