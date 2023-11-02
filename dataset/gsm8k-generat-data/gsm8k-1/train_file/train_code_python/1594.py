def solution():
    """With 40 seconds left to play in the basketball game, the Dunkinville Hornets were leading the Fredingo Fireflies by a score of 86 to 74. In the remaining seconds in the game, the Fireflies scored 7 three-point baskets while holding the Hornets to only 2 two-point baskets to win the game. How many more points did the Fireflies score in the game than did the Hornets?"""
    hornets_score = 86
    fireflies_score = 74
    three_pointer_score = 3
    two_pointer_score = 2
    fireflies_score += 7 * three_pointer_score
    hornets_score += 2 * two_pointer_score
    point_difference = fireflies_score - hornets_score
    result = point_difference
    return result

print(solution())