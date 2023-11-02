def solution():
    # Calculate the time Dante spent walking to and from Hidden Lake
    hidden_lake_time = 15 + 7

    # Calculate the remaining time Dante has been gone from the Park Office
    remaining_time = 32 - hidden_lake_time

    # Calculate the time Dante spent walking to the Lake Park restaurant
    restaurant_time = remaining_time - 15

    result = restaurant_time
    return result

print(solution())