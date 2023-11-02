def solution():
    # Define the distances Nina travels
    normal_distance = 400
    double_distance = 2 * normal_distance

    # Calculate the total distance Nina travels in 2 years
    total_distance = 0
    for i in range(24):
        if i % 2 == 0:
            total_distance += double_distance
        else:
            total_distance += normal_distance

    result = total_distance
    return result

print(solution())