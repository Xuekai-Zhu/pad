def solution():
    """Tyson can swim at a speed of 3 miles per hour in a lake and 2.5 mph in an ocean. This season, half his races happened in lakes and half his races happened in the ocean. He had ten total races, each of which was 3 miles long. How much time did he spend in his races?"""
    lake_speed = 3
    ocean_speed = 2.5
    race_distance = 3
    lake_races = 5
    ocean_races = 5
    lake_time = (race_distance / lake_speed) * lake_races
    ocean_time = (race_distance / ocean_speed) * ocean_races
    total_time = lake_time + ocean_time
    result = total_time
    return result

print(solution())