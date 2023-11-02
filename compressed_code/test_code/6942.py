def solution():
    
    daily_jogging_time = 30/60 
    tuesday_jogging_time = (30+5)/60 
    friday_jogging_time = (30+25)/60 
    total_jogging_time = (daily_jogging_time * 3) + tuesday_jogging_time + friday_jogging_time 
    result = total_jogging_time
    return result

print(solution())