def solution():
    num_days = 7
    num_pushups_first_day = 10
    pushup_increase = 5
    total_pushups = num_pushups_first_day
    
    for i in range(1, num_days):
        total_pushups += (num_pushups_first_day + (pushup_increase * i))
    
    result = total_pushups
    return result

print(solution())