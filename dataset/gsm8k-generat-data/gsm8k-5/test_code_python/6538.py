def solution():
    total_distance = 900  # The entire path is 900 feet long
    pole_distance = 6  # A fence pole is placed every 6 feet
    bridge_length = 42  # A 42-foot bridge is excluded from the fence

    # Calculate the total distance covered with fence poles
    fence_distance = total_distance - bridge_length

    # Calculate the number of fence poles needed
    num_poles = fence_distance / pole_distance

    # Since there are poles on both sides, multiply by 2
    num_poles *= 2

    result = num_poles
    return result

print(solution())