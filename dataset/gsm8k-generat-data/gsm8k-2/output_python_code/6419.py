def solution():
    """Rich likes to take long walks through town. First he walks 20 feet from his house to the sidewalk. Then he walks 200 feet down the sidewalk to the end of the road. Then he makes a left and walks double his total distance so far until he reaches the next intersection. Then he walks half the total distance up to this point again to the end of his route, before turning around and walking the same path all the way back home. How many feet did Rich walk?"""
    distance_from_home = 20
    sidewalk_distance = 200
    left_distance = 2 * (distance_from_home + sidewalk_distance)
    total_distance = distance_from_home + sidewalk_distance + left_distance + (left_distance + distance_from_home) / 2
    total_distance *= 2  # round-trip
    result = total_distance
    return result

print(solution())