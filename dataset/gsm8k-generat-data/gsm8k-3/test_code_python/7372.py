def solution():
    """A plane flies between 4 cities; A, B, C and D. Passengers board and alight at each airport in every city when it departs and lands, respectively.  The distance between city A and city B is 100 miles.  The distance between city B and city C is 50 miles more than the distance between city A and city B.  The distance between city C and city D is twice the distance between city B and city C. Calculate the total distance between city A and city D."""
    # Define the distance between city A and city B
    AB_distance = 100

    # Define the distance between city B and city C
    BC_distance = AB_distance + 50

    # Define the distance between city C and city D
    CD_distance = 2 * BC_distance

    # Calculate the total distance between city A and city D
    total_distance = AB_distance + BC_distance + CD_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())