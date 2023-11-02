def solution():
    """Tammy wants to run 3500 meters per week. She knows her track at school is 50 meters around. If she wants to run the same amount each day, how many loops should she make per day?"""
    weekly_distance = 3500
    daily_distance = weekly_distance / 7
    loop_distance = 50
    loops_per_day = daily_distance / loop_distance
    result = loops_per_day
    return result

print(solution())