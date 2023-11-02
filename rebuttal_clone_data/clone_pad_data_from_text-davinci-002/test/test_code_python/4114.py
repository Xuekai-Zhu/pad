def solution():
    initial_pollywogs = 2400
    pollywogs_lost_per_day = 50
    pollywogs_removed_per_day = 10
    days = 0
    
    while initial_pollywogs > 0:
        initial_pollywogs -= pollywogs_lost_per_day
        if days < 20:
            initial_pollywogs -= pollywogs_removed_per_day
        days += 1
    result = days
    return result

print(solution())