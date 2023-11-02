def solution():
    """Tammy wants to run 3500 meters per week. She knows her track at school is 50 meters around. If she wants to run the same amount each day, how many loops should she make per day?"""
    # Define the distance Tammy wants to run per week
    distance_per_week = 3500

    # Define the distance of each loop on the track
    loop_distance = 50

    # Calculate the number of loops Tammy needs to run per week
    loops_per_week = distance_per_week / loop_distance

    # Calculate the number of loops Tammy needs to run per day
    loops_per_day = loops_per_week / 7

    # Display the number of loops Tammy needs to run per day
    result = loops_per_day
    return result

print(solution())