def solution():
    minutes = 10
    cups_per_minute = 2
    first_30_minutes = 30
    cups_first_30_minutes = minutes * cups_per_minute * first_30_minutes
    next_30_minutes = 30
    cups_next_30_minutes = minutes * cups_per_minute * next_30_minutes
    following_hour = 60
    cups_per_minute_max = 4
    cups_following_hour = minutes * cups_per_minute_max * following_hour
    total_cups = cups_first_30_minutes + cups_next_30_minutes + cups_following_hour
    cups_dumped = total_cups / 2
    cups_left = total_cups - cups_dumped
    result = cups_left
    
    return result

print(solution())