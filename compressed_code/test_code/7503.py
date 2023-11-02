def solution():
    
    turns_per_30_seconds = 6
    seconds_per_hour = 3600 
    turns_per_hour = turns_per_30_seconds * (seconds_per_hour / 30)
    turns_in_two_hours = turns_per_hour * 2
    result = turns_in_two_hours
    return result

print(solution())