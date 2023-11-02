def solution():
    total_height = 1673  # given height of Taipei 101
    num_floors = 101  # given number of floors
    height_per_floor = 16.5  # given height of floors from 1st to 100th floor

    # Calculate total height of first to 100th floors
    total_height_100floors = (num_floors-1) * height_per_floor

    # Calculate height of 101st floor by subtracting total height of 1st to 100th floors from the total height of building
    height_101st_floor = total_height - total_height_100floors
    result = height_101st_floor
    return result

print(solution())