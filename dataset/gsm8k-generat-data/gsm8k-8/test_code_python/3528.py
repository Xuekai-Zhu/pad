def solution():
    # Convert the number of dozens of water bottles to the total number of water bottles
    num_water_bottles = 4 * 12

    # Calculate the total number of water bottles used by the players
    total_used = 11 * 2 + 11

    # Calculate the number of water bottles remaining
    remaining_bottles = num_water_bottles - total_used
    result = remaining_bottles
    return result

print(solution())