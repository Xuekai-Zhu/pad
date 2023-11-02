def solution():
    # Define the variables
    distance_per_block = 200
    johnny_blocks = 4
    mickey_blocks = johnny_blocks / 2

    # Calculate the total distance run by Johnny and Mickey
    johnny_distance = johnny_blocks * distance_per_block
    mickey_distance = mickey_blocks * distance_per_block
    total_distance = johnny_distance + mickey_distance

    # Calculate the average distance run
    average_distance = total_distance / 2
    result = average_distance
    return result

print(solution())