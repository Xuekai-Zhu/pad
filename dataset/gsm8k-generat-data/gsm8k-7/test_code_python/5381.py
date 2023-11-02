def solution():
    distance_per_block = 200
    johnny_blocks = 4
    mickey_blocks = johnny_blocks/2

    # Calculate the total distance run by Johnny
    johnny_distance = johnny_blocks * distance_per_block

    # Calculate the total distance run by Mickey
    mickey_distance = mickey_blocks * distance_per_block

    # Calculate the average distance run by Johnny and Mickey
    avg_distance = (johnny_distance + mickey_distance) / 2
    result = avg_distance
    return result

print(solution())