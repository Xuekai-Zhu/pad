def solution():
    """Mickey and Johnny are having a contest to see who can run around their block the most. One time around the block equals 200 meters. Johnny runs around the block 4 times. Mickey runs around the block half as many times as Johnny. What is the average distance run by Johnny and Mickey?"""
    block_distance = 200
    johnny_distance = 4 * block_distance
    mickey_distance = 0.5 * johnny_distance
    total_distance = johnny_distance + mickey_distance
    average_distance = total_distance / 2
    result = average_distance
    return result

print(solution())