def solution():
    hornets_score = 86  # Hornets had a score of 86 points
    fireflies_score = 74  # Fireflies had a score of 74 points
    fireflies_score += (7 * 3)  # Fireflies scored 7 three-point baskets, which increased their score by 21 points
    hornets_score += (2 * 2)  # Hornets scored 2 two-point baskets, which increased their score by 4 points

    # Calculate the difference in scores between the Fireflies and the Hornets
    score_difference = fireflies_score - hornets_score
    result = score_difference
    return result

print(solution())