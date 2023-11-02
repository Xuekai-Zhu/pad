def solution():
    """Ayen jogs for 30 minutes every day during weekdays. This week on Tuesday, she jogged 5 minutes more and also jogged 25 minutes more on Friday. How many hours, in total, did Ayen jog this week?"""
    daily_jogging_time = 30/60 # convert minutes to hours
    tuesday_jogging_time = (30+5)/60 # add 5 minutes to Tuesday's time and convert to hours
    friday_jogging_time = (30+25)/60 # add 25 minutes to Friday's time and convert to hours
    total_jogging_time = (daily_jogging_time * 3) + tuesday_jogging_time + friday_jogging_time # jog for 3 weekdays and add Tuesday and Friday
    result = total_jogging_time
    return result

print(solution())