def solution():
    # Define the time it takes for Derek to walk a mile alone and with his brother
    time_alone = 9
    time_with_brother = 12

    # Calculate the time difference
    time_difference = time_with_brother - time_alone

    # Calculate the extra time it would take to walk 20 miles with his brother
    extra_time = time_difference * 20

    result = extra_time
    return result

print(solution())