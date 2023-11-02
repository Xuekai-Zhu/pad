def solution():
    """Ken likes to bike when it's raining and can cycle 30 miles in 20 minutes during this time. However, when it's snowing Ken can't stand the cold and can only cycle 10 miles in 20 minutes. If it rains 3 times and snows 4 times in one week, how many miles did Ken reach if he cycles 1 hour a day?"""
    # Define the distances traveled in rain and snow
    rain_distance = 30
    snow_distance = 10

    # Calculate the total time spent biking in a week
    total_time = 7 * 60

    # Calculate the total distance traveled during rain and snow
    total_rain_distance = rain_distance * 3
    total_snow_distance = snow_distance * 4

    # Calculate the remaining time and distance
    remaining_time = total_time - (3 + 4) * 20
    remaining_distance = remaining_time / 20 * rain_distance

    # Calculate the total distance traveled in a week
    total_distance = total_rain_distance + total_snow_distance + remaining_distance

    # Calculate the distance traveled in one hour
    distance_per_hour = total_distance / (total_time / 60)

    # Round the result to 2 decimal places
    result = round(distance_per_hour, 2)
    return result

print(solution())