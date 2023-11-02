def solution():
    # Calculate the total distance traveled on the first four coasters
    total_distance = (50 + 62 + 73 + 70) * 5

    # Calculate the speed of the fifth coaster to maintain an average of 59 mph for the day
    fifth_coaster_speed = (59 * 5 - total_distance) / 5
    result = fifth_coaster_speed
    return result

print(solution())