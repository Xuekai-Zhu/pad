def solution():
    """Mickey and Johnny are having a contest to see who can run around their block the most. One time around the block equals 200 meters. Johnny runs around the block 4 times. Mickey runs around the block half as many times as Johnny. What is the average distance run by Johnny and Mickey?"""
    # Define the distance for one time around the block
    BLOCK_DISTANCE = 200

    # Calculate the distance run by Johnny
    johnny_distance = 4 * BLOCK_DISTANCE

    # Calculate the distance run by Mickey
    mickey_distance = 0.5 * johnny_distance

    # Calculate the total distance run by both
    total_distance = johnny_distance + mickey_distance

    # Calculate the average distance run by both
    average_distance = total_distance / 2

    # Display the average distance run by both
    result = average_distance
    return result

print(solution())