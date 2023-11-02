def solution():
    weekly_distance = 3500  # Tammy wants to run 3500 meters per week
    track_distance = 50  # The track at school is 50 meters around

    # Calculate the number of loops Tammy needs to make per week
    loops_per_week = weekly_distance / track_distance

    # Calculate the number of loops Tammy needs to make per day
    loops_per_day = loops_per_week / 7
    result = loops_per_day
    return result

print(solution())