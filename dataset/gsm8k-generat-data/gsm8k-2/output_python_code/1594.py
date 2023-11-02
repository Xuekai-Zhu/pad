def solution():
    """With 40 seconds left to play in the basketball game, the Dunkinville Hornets were leading the Fredingo Fireflies by a score of 86 to 74. In the remaining seconds in the game, the Fireflies scored 7 three-point baskets while holding the Hornets to only 2 two-point baskets to win the game. How many more points did the Fireflies score in the game than did the Hornets?"""
    hornets_points = 86
    fireflies_points = 74
    hornets_points += 2*2  # add 2 two-point baskets for Hornets
    fireflies_points += 7*3  # add 7 three-point baskets for Fireflies
    difference = fireflies_points - hornets_points  # calculate the difference
    result = difference
    return result

print(solution())