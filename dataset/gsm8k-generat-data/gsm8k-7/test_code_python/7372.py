def solution():
    distance_AB = 100
    distance_BC = distance_AB + 50
    distance_CD = distance_BC * 2

    # Calculate the total distance between city A and city D
    total_distance = distance_AB + distance_BC + distance_CD
    result = total_distance
    return result

print(solution())