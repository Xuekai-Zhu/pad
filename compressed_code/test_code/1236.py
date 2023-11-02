def solution():
    
    monthly_goal = 400
    every_other_month_goal = monthly_goal * 2
    total_distance = 0
    for i in range(24):
        if i % 2 == 1:
            total_distance += every_other_month_goal
        else:
            total_distance += monthly_goal
    
    result = total_distance
    return result

print(solution())