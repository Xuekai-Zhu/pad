def solution():
    distance_AB = 100  # Distance between city A and city B is 100 miles
    distance_BC = distance_AB + 50  # Distance between city B and city C is 50 miles more than between city A and city B
    distance_CD = 2 * distance_BC  # Distance between city C and city D is twice the distance between city B and city C

    # Calculate the total distance between city A and city D
    total_distance = distance_AB + distance_BC + distance_CD
    result = total_distance
    return result

print(solution())