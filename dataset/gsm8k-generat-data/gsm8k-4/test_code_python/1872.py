def solution():
    """20 birds migrate on a seasonal basis from one lake to another, searching for food. If they fly from lake Jim to lake Disney in one season, which is 50 miles apart, then the next season they fly from lake Disney to lake London, 60 miles apart, calculate the combined distance all of the birds have traveled in the two seasons."""
    # Define the distance between lake Jim and lake Disney and the distance between lake Disney and lake London
    distance_jim_disney = 50
    distance_disney_london = 60

    # Calculate the total distance traveled by all birds in the two seasons
    total_distance = 20 * (distance_jim_disney + distance_disney_london)

    # return the result
    result = total_distance
    return result

print(solution())