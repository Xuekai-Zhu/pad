def solution():
    """Ken likes to bike when it's raining and can cycle 30 miles in 20 minutes during this time. However, when it's snowing Ken can't stand the cold and can only cycle 10 miles in 20 minutes. If it rains 3 times and snows 4 times in one week, how many miles did Ken reach if he cycles 1 hour a day?"""
    # Define the time Ken spends biking
    biking_time = 1 * 60 # 1 hour = 60 minutes

    # Define the distance Ken travels in different weather conditions
    RAIN_DISTANCE = 30
    SNOW_DISTANCE = 10

    # Define the number of times it rains and snows in one week
    RAIN_COUNT = 3
    SNOW_COUNT = 4

    # Calculate the total distance Ken bikes in one week
    rain_distance = RAIN_DISTANCE * RAIN_COUNT
    snow_distance = SNOW_DISTANCE * SNOW_COUNT
    total_distance = (rain_distance + snow_distance) * (biking_time / 20)

    # Display the total distance biked in one week
    result = total_distance
    return result

print(solution())