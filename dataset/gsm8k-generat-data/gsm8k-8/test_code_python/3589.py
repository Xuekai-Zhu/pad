def solution():
    # Calculate the time it takes to travel 200 miles with the 24 sq. ft. sail
    time_with_big_sail = 200 / 50

    # Calculate the time it takes to travel 200 miles with the 12 sq. ft. sail
    time_with_small_sail = 200 / 20

    # Calculate the difference in time between the two sails
    time_difference = time_with_small_sail - time_with_big_sail

    result = time_difference
    return result

print(solution())