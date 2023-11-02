def solution():
    # Calculate the time Chris spends walking to school
    time_chris = 9 / 3  # Chris walks 3 miles per hour

    # Calculate the distance Mark walks before turning around
    distance_mark = 3

    # Calculate the time Mark spends walking
    time_mark = (distance_mark * 2) / 3  # Mark walks at the same speed as Chris

    # Calculate the difference in time between Mark and Chris
    diff_time = time_mark - time_chris

    result = diff_time
    return result

print(solution())