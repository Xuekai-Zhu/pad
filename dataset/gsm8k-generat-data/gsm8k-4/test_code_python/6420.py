def solution():
    """Rich likes to take long walks through town. First he walks 20 feet from his house to the sidewalk. Then he walks 200 feet down the sidewalk to the end of the road. Then he makes a left and walks double his total distance so far until he reaches the next intersection. Then he walks half the total distance up to this point again to the end of his route, before turning around and walking the same path all the way back home. How many feet did Rich walk?"""
    # Define the distances of each segment of the walk
    distance_1 = 20
    distance_2 = 200
    distance_3 = distance_2 * 2
    distance_4 = (distance_1 + distance_2 + distance_3) * 0.5

    # Calculate the total distance of the walk
    total_distance = distance_1 + distance_2 + distance_3 + distance_4
    # Multiply by 2 for the return trip
    total_distance *= 2

    result = total_distance
    return result

print(solution())