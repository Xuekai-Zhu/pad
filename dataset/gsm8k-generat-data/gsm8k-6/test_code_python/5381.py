def solution():
    # Calculate the total distance run by Johnny and Mickey
    distance_Johnny = 4 * 200  # Johnny runs around the block 4 times
    distance_Mickey = (1/2) * distance_Johnny  # Mickey runs around the block half as many times as Johnny
    total_distance = distance_Johnny + distance_Mickey

    # Calculate the average distance run by Johnny and Mickey
    average_distance = total_distance / 2

    result = average_distance
    return result

print(solution())