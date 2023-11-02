def solution():
    speed = 10 # miles per hour
    time_first_leg = 30 / 60 # 30 minutes = 0.5 hours
    distance_second_leg = 15 # miles
    rest_time = 30 # minutes
    distance_third_leg = 20 # miles

    # Calculate the time taken for the first leg
    time_first_leg = distance_first_leg / speed

    # Calculate the time taken for the second leg
    time_second_leg = (distance_second_leg / speed) * 60

    # Add rest time to total time
    total_time = time_first_leg + time_second_leg + rest_time

    # Calculate the time taken for the third leg
    time_third_leg = (distance_third_leg / speed) * 60

    # Add time taken for third leg to total time
    total_time += time_third_leg

    result = total_time
    return result

print(solution())