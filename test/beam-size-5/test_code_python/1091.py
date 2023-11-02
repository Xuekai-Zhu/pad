def solution():
    # Calculate the distance traveled by the first train in 3 hours
    distance_train1 = 60 * 3

    # Calculate the distance traveled by the second train in 3 hours
    distance_train2 = 0.5 * 60 * 3

    # Calculate the total distance traveled by both trains in 3 hours
    total_distance = distance_train1 + distance_train2
    result = total_distance
    return result

print(solution())