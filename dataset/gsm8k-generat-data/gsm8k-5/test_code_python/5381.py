def solution():
    distance_per_block = 200  # Each block is 200 meters
    johnny_blocks = 4  # Johnny runs around the block 4 times
    mickey_blocks = johnny_blocks / 2  # Mickey runs around the block half as many times as Johnny

    # Calculate the distance run by Johnny and Mickey
    johnny_distance = johnny_blocks * distance_per_block
    mickey_distance = mickey_blocks * distance_per_block

    # Calculate the average distance run by Johnny and Mickey
    average_distance = (johnny_distance + mickey_distance) / 2
    result = average_distance
    return result

print(solution())