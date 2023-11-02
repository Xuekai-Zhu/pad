def solution():
    distance_AB = 100  # distance between city A and city B is 100 miles
    distance_BC = 100 + 50  # distance between city B and city C is 50 miles more than the distance between city A and city B
    distance_CD = 2 * distance_BC  # distance between city C and city D is twice the distance between city B and city C
    total_distance = distance_AB + distance_BC + distance_CD  # total distance between city A and city D
    result = total_distance
    return result

print(solution())