def solution():
    # Calculate the total time Dante spends walking to and from Hidden Lake
    total_time = 15 + 7  # minutes

    # Calculate how long Dante was at the Park Office before and after the walk
    office_time = 32 - total_time  # minutes

    # Calculate how long Dante spent walking to the Lake Park restaurant
    restaurant_time = office_time / 2

    result = restaurant_time
    return result

print(solution())