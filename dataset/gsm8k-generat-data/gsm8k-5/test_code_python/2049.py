def solution():
    distance_to_school = 9  # Distance from their house to school is 9 miles
    walking_speed = 3  # Both Mark and Chris walk at a speed of 3 miles per hour

    # Calculate the time it takes for Chris to walk to school
    time_for_chris = distance_to_school / walking_speed

    # Calculate the time it takes for Mark to reach the point where he forgot his lunch
    time_for_mark_to_forget_lunch = 3 / walking_speed

    # Calculate the time Mark spends walking after forgetting his lunch
    time_for_mark_after_forgetting_lunch = (distance_to_school - 3) / walking_speed

    # Calculate the total time Mark spends walking
    total_time_for_mark = time_for_mark_to_forget_lunch + time_for_mark_after_forgetting_lunch

    # Calculate the difference in time between Mark and Chris
    time_difference = total_time_for_mark - time_for_chris
    result = time_difference
    return result

print(solution())