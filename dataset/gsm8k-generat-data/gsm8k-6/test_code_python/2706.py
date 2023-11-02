def solution():
    # Calculate the net forward movement of the leaf after 11 gusts of wind
    forward_movement = 11 * 5  # for every 5 feet forward, the wind blows it back 2 feet, so the net forward movement is 3 feet per gust
    backward_movement = 11 * 2
    net_movement = forward_movement - backward_movement
    result = net_movement
    return result

print(solution())