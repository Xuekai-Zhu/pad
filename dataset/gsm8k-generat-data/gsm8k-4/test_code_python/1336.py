def solution():
    """It takes Jason 30 minutes to cut 1 lawn in his neighborhood. If he cuts 8 yards on both Saturday and Sunday, how many hours does he spend cutting grass?"""
    # Define the time it takes to cut one lawn
    time_per_lawn = 0.5  # in hours

    # Define the number of lawns cut on Saturday and Sunday
    lawns_per_day = 8

    # Calculate the total time spent cutting grass
    total_time = time_per_lawn * lawns_per_day * 2  # 2 days of cutting

    # Return the total time spent in hours
    result = total_time
    return result

print(solution())