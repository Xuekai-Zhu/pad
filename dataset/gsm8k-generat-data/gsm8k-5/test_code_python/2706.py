def solution():
    forward_distance = 5  # the wind blows the leaf forward for 5 feet
    backward_distance = 2  # for every 5 feet forward, the wind blows the leaf back 2 feet
    gusts = 11  # the leaf experiences 11 gusts of wind

    # Calculate the net distance covered after each full cycle of 5 feet forward and 2 feet back
    net_distance = forward_distance - backward_distance
    
    # Calculate the total net distance covered after all gusts of wind
    total_distance = net_distance * (gusts // 3) * 3  # using integer division to round down to the nearest full cycle of 3 gusts
    remaining_gusts = gusts % 3
    
    # Calculate the remaining net distance covered
    if remaining_gusts == 1:
        total_distance += forward_distance
    elif remaining_gusts == 2:
        total_distance += forward_distance + net_distance
    
    result = total_distance
    return result

print(solution())