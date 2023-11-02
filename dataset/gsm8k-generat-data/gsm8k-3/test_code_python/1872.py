def solution():
    """20 birds migrate on a seasonal basis from one lake to another,
    searching for food. If they fly from lake Jim to lake Disney in one
    season, which is 50 miles apart, then the next season they fly from
    lake Disney to lake London, 60 miles apart, calculate the combined
    distance all of the birds have traveled in the two seasons."""
    # Calculate the distance traveled by the birds in the first season
    season1_distance = 20 * 50

    # Calculate the distance traveled by the birds in the second season
    season2_distance = 20 * 60

    # Calculate the total distance traveled by the birds
    total_distance = season1_distance + season2_distance

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())