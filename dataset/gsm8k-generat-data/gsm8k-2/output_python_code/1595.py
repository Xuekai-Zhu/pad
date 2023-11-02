def solution():
    """Nina loves to travel. She tries to travel at least 400 kilometers in one month outside of her home country. Every second month she does twice that distance. If she were able to keep up with her resolution, how many kilometers would she travel during 2 years?"""
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