def solution():
    # Define the distance traveled by each gust of wind
    forward_distance = 5
    backward_distance = 2

    # Calculate the net distance traveled by 11 gusts
    net_distance = 11 * (forward_distance - backward_distance)

    # Calculate the total distance traveled by adding the net distance to the starting distance of 0
    total_distance = net_distance + 0

    result = total_distance
    return result

print(solution())