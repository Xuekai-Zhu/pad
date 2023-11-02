def solution():
    """Tyson can swim at a speed of 3 miles per hour in a lake and 2.5 mph in an ocean. This season, half his races happened in lakes and half his races happened in the ocean. He had ten total races, each of which was 3 miles long. How much time did he spend in his races?"""
    # Define the swimming speed in the lake and ocean
    lake_speed = 3  # miles per hour
    ocean_speed = 2.5  # miles per hour

    # Define the distance to swim for each race
    distance = 3  # miles

    # Calculate the number of races in each location
    lake_races = 5
    ocean_races = 5

    # Calculate the time spent swimming in each location
    lake_time = distance / lake_speed
    ocean_time = distance / ocean_speed

    # Calculate the total time spent in all races
    total_time = (lake_races * lake_time) + (ocean_races * ocean_time)

    # return the result
    result = total_time
    return result

print(solution())