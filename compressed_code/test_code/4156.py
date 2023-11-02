def solution():
    
    block_distance = 200
    johnny_distance = 4 * block_distance
    mickey_distance = 0.5 * johnny_distance
    total_distance = johnny_distance + mickey_distance
    average_distance = total_distance / 2
    result = average_distance
    return result

print(solution())