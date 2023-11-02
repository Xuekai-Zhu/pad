def solution():
    """Rich likes to take long walks through town.  First he walks 20 feet from his house to the sidewalk.  Then he walks 200 feet down the sidewalk to the end of the road.  Then he makes a left and walks double his total distance so far until he reaches the next intersection.  Then he walks half the total distance up to this point again to the end of his route, before turning around and walking the same path all the way back home.  How many feet did Rich walk?"""
    # Define the distances of each segment of Rich's walk
    distance1 = 20
    distance2 = 200
    distance3 = distance2 * 2
    distance4 = (distance1 + distance2 + distance3) / 2
    total_distance = (distance1 + distance2 + distance3 + distance4) * 2

    # Display the total distance
    result = total_distance
    return result

print(solution())