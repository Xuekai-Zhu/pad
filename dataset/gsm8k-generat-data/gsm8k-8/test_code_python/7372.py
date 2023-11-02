def solution():
    # Define the distances between the cities
    distance_AB = 100
    distance_BC = distance_AB + 50
    distance_CD = 2 * distance_BC

    # Calculate the total distance
    total_distance = distance_AB + distance_BC + distance_CD
    result = total_distance
    return result

print(solution())