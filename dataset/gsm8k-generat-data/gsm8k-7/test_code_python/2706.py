def solution():
    gust_forward = 5
    gust_backward = 2
    num_gusts = 11

    # Calculate the total distance traveled by the leaf
    total_distance = 0
    for i in range(num_gusts):
        total_distance += gust_forward
        total_distance -= gust_backward

    result = total_distance
    return result

print(solution())