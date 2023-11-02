def solution():
    
    lion_meat_per_day = 25
    tiger_meat_per_day = 20
    total_meat = 90
    total_meat_per_day = lion_meat_per_day + tiger_meat_per_day
    days = total_meat / total_meat_per_day
    result = days
    return result

print(solution())