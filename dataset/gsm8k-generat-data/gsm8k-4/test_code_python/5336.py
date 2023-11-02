def solution():
    """Tammy wants to run 3500 meters per week. She knows her track at school is 50 meters around. If she wants to run the same amount each day, how many loops should she make per day?"""
    # Define the total distance Tammy wants to run per week and the distance of the track
    weekly_distance = 3500
    track_distance = 50

    # Calculate the number of loops Tammy needs to run each week
    loops_per_week = weekly_distance / track_distance

    # Calculate the number of loops Tammy needs to run each day
    loops_per_day = loops_per_week / 7

    # Round up to the nearest whole number
    loops_per_day = int(round(loops_per_day, 0))

    # Return the result
    result = loops_per_day
    return result

print(solution())