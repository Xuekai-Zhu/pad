def solution():
    """Rich likes to take long walks through town. First he walks 20 feet from his house to the sidewalk. Then he walks 200 feet down the sidewalk to the end of the road. Then he makes a left and walks double his total distance so far until he reaches the next intersection. Then he walks half the total distance up to this point again to the end of his route, before turning around and walking the same path all the way back home. How many feet did Rich walk?"""
    distance_from_house_to_sidewalk = 20
    distance_down_sidewalk = 200
    distance_to_next_intersection = distance_down_sidewalk * 2
    distance_to_end_of_route = (distance_down_sidewalk + distance_to_next_intersection) * 0.5
    total_distance = 2 * (distance_from_house_to_sidewalk + distance_down_sidewalk + distance_to_next_intersection + distance_to_end_of_route)
    result = total_distance
    return result

print(solution())