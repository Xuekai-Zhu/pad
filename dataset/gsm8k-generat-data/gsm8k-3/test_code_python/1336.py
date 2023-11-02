def solution():
    """It takes Jason 30 minutes to cut 1 lawn in his neighborhood.  If he cuts 8 yards on both Saturday and Sunday, how many hours does he spend cutting grass?"""
    # Define the time it takes Jason to cut 1 lawn
    TIME_PER_LAWN = 0.5 # in hours (30 minutes)

    # Define the number of lawns Jason cuts on each day
    LAWNS_PER_DAY = 8

    # Calculate the total time Jason spends cutting grass
    total_time = TIME_PER_LAWN * LAWNS_PER_DAY * 2 # 2 days

    # Display the total time
    result = total_time
    return result

print(solution())