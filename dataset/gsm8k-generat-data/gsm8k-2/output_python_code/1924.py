def solution():
    """Tyson can swim at a speed of 3 miles per hour in a lake and 2.5 mph in an ocean. This season, half his races happened in lakes and half his races happened in the ocean. He had ten total races, each of which was 3 miles long. How much time did he spend in his races?"""
    lake_distance = 1.5 * 3  # Half of the races were in lakes, and each race was 3 miles long
    ocean_distance = 1.5 * 3  # Half of the races were in oceans, and each race was 3 miles long
    lake_speed = 3
    ocean_speed = 2.5
    lake_time = lake_distance / lake_speed
    ocean_time = ocean_distance / ocean_speed
    total_time = lake_time + ocean_time
    result = total_time
    return result

print(solution())