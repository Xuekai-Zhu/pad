def solution():
    """A plane flies between 4 cities; A, B, C and D. Passengers board and alight at each airport in every city when it departs and lands, respectively. The distance between city A and city B is 100 miles. The distance between city B and city C is 50 miles more than the distance between city A and city B. The distance between city C and city D is twice the distance between city B and city C. Calculate the total distance between city A and city D."""
    # Define the distance between cities A and B
    distance_AB = 100

    # Define the distance between cities B and C
    distance_BC = distance_AB + 50

    # Define the distance between cities C and D
    distance_CD = distance_BC * 2

    # Calculate the total distance traveled by the plane
    total_distance = distance_AB + distance_BC + distance_CD

    result = total_distance
    return result

print(solution())