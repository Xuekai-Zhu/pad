def solution():
    """20 birds migrate on a seasonal basis from one lake to another, searching for food. If they fly from lake Jim to lake Disney in one season, which is 50 miles apart, then the next season they fly from lake Disney to lake London, 60 miles apart, calculate the combined distance all of the birds have traveled in the two seasons."""
    birds = 20
    jim_to_disney = 50
    disney_to_london = 60
    combined_distance = (jim_to_disney + disney_to_london) * birds
    result = combined_distance
    return result

print(solution())