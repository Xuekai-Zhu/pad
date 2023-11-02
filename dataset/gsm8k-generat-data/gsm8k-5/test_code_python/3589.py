def solution():
    distance = 200  # Danny plans to travel 200 miles

    # Time taken with the 24 sq ft sail
    time_big_sail = distance / 50

    # Time taken with the 12 sq ft sail
    time_small_sail = distance / 20

    # Difference in time taken between bigger sail and smaller sail
    time_difference = time_small_sail - time_big_sail

    # Convert time difference to hours and round off to 2 decimal places
    hours_difference = round(abs(time_difference), 2)

    result = hours_difference
    return result

print(solution())