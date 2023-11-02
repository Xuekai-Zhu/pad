def solution():
    """Tyson can swim at a speed of 3 miles per hour in a lake and 2.5 mph in an ocean. This season, half his races happened in lakes and half his races happened in the ocean. He had ten total races, each of which was 3 miles long. How much time did he spend in his races?"""
    # Define Tyson's speed in the lake and ocean
    LAKE_SPEED = 3
    OCEAN_SPEED = 2.5

    # Define the distance of each race
    DISTANCE = 3

    # Calculate the total time spent in lake races
    lake_time = (10 / 2) * (DISTANCE / LAKE_SPEED)

    # Calculate the total time spent in ocean races
    ocean_time = (10 / 2) * (DISTANCE / OCEAN_SPEED)

    # Calculate the total time spent in all races
    total_time = lake_time + ocean_time

    # Display the total time spent
    result = total_time
    return result

print(solution())