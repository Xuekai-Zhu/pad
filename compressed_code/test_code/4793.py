def solution():
    
    dec_sleep = 6.5
    jan_sleep = 8.5
    days_jan = 31
    more_sleep_per_night = jan_sleep - dec_sleep
    total_more_sleep = more_sleep_per_night * days_jan
    result = total_more_sleep
    return result

print(solution())