def solution():
    """Mickey and Johnny are having a contest to see who can run around their block the most. One time around the block equals 200 meters. Johnny runs around the block 4 times. Mickey runs around the block half as many times as Johnny. What is the average distance run by Johnny and Mickey?"""
    
    # Define the distance of one time around the block
    DISTANCE_PER_BLOCK = 200
    
    # Calculate the distance run by Johnny
    johnny_blocks = 4
    johnny_distance = johnny_blocks * DISTANCE_PER_BLOCK
    
    # Calculate the distance run by Mickey
    mickey_blocks = johnny_blocks / 2
    mickey_distance = mickey_blocks * DISTANCE_PER_BLOCK
    
    # Calculate the average distance run by both
    total_distance = johnny_distance + mickey_distance
    average_distance = total_distance / 2
    
    # Return the result
    result = average_distance
    return result

print(solution())