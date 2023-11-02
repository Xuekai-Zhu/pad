def solution():
    # Calculate the total distance Bess has thrown the Frisbee
    bess_distance = 20 * 4  # Bess can throw the Frisbee 20 meters, and she does this 4 times
    # Each time Bess throws the Frisbee, she throws it back to her original position, so this distance is not added.

    # Calculate the total distance Holly has thrown the Frisbee
    holly_distance = 8 * 5  # Holly can throw the Frisbee 8 meters, and she does this 5 times
    # Holly leaves her Frisbee where it lands every time she throws it, so this distance is not added.

    # Calculate the total distance the thrown Frisbees have traveled
    total_distance = bess_distance + holly_distance
    result = total_distance
    return result

print(solution())