def solution():
    """With 40 seconds left to play in the basketball game, the Dunkinville Hornets were leading the Fredingo Fireflies by a score of 86 to 74. In the remaining seconds in the game, the Fireflies scored 7 three-point baskets while holding the Hornets to only 2 two-point baskets to win the game. How many more points did the Fireflies score in the game than did the Hornets?"""
    # Define the initial score
    hornets_score = 86
    fireflies_score = 74

    # Define the number of points scored on each basket
    three_point_basket = 3
    two_point_basket = 2

    # Calculate the points scored by the Fireflies in the remaining seconds
    fireflies_points = 7 * three_point_basket

    # Calculate the points scored by the Hornets in the remaining seconds
    hornets_points = 2 * two_point_basket

    # Update the final score
    hornets_score += hornets_points
    fireflies_score += fireflies_points

    # Calculate the difference in points
    difference = fireflies_score - hornets_score

    result = difference
    return result

print(solution())