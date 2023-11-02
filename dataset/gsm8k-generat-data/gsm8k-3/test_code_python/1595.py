def solution():
    """With 40 seconds left to play in the basketball game, the Dunkinville Hornets were leading the Fredingo Fireflies by a score of 86 to 74.  In the remaining seconds in the game, the Fireflies scored 7 three-point baskets while holding the Hornets to only 2 two-point baskets to win the game.  How many more points did the Fireflies score in the game than did the Hornets?"""
    
    # Calculate the points scored by the Fireflies in the last 40 seconds
    fireflies_last_40_seconds = 7 * 3

    # Calculate the points scored by the Hornets in the last 40 seconds
    hornets_last_40_seconds = 2 * 2

    # Calculate the total points scored by the Fireflies
    total_fireflies_points = 86 + fireflies_last_40_seconds

    # Calculate the total points scored by the Hornets
    total_hornets_points = 74 + hornets_last_40_seconds

    # Calculate the difference in points between the Fireflies and the Hornets
    point_difference = total_fireflies_points - total_hornets_points

    # Display the point difference
    result = point_difference
    return result

print(solution())