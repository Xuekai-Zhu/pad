def solution():
    
    rabbit_weekly_cost = 12
    parrot_weekly_cost = 30 - rabbit_weekly_cost
    rabbit_duration = 5
    parrot_duration = 3
    rabbit_total_cost = rabbit_weekly_cost * rabbit_duration
    parrot_total_cost = parrot_weekly_cost * parrot_duration
    total_cost = rabbit_total_cost + parrot_total_cost
    result = total_cost
    return result

print(solution())