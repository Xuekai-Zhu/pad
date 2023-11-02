def solution():
    """A plane flies between 4 cities; A, B, C and D. Passengers board and alight at each airport in every city when it departs and lands, respectively. The distance between city A and city B is 100 miles. The distance between city B and city C is 50 miles more than the distance between city A and city B. The distance between city C and city D is twice the distance between city B and city C. Calculate the total distance between city A and city D."""
    distance_AB = 100
    distance_BC = distance_AB + 50
    distance_CD = 2 * distance_BC
    total_distance = distance_AB + distance_BC + distance_CD
    result = total_distance
    return result

print(solution())