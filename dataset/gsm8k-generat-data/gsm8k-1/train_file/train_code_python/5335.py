def solution():
    """Tammy wants to run 3500 meters per week. She knows her track at school is 50 meters around. If she wants to run the same amount each day, how many loops should she make per day?"""
    total_meters_per_week = 3500
    meters_per_loop = 50
    loops_per_day = total_meters_per_week / (meters_per_loop * 7)
    result = loops_per_day
    return result

print(solution())