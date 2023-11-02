def solution():
    hornets_score = 86
    fireflies_score = 74

    # Calculate the points scored by Fireflies with 7 three-point baskets
    fireflies_score += (7 * 3)

    # Calculate the points scored by Hornets with 2 two-point baskets
    hornets_score += (2 * 2)

    # Calculate the difference in scores between Fireflies and Hornets
    score_difference = fireflies_score - hornets_score
    result = score_difference
    return result

print(solution())