def solution():
    # Calculate the total points scored by the Fireflies in the remaining 40 seconds
    fireflies_points = 7 * 3  # 7 three-point baskets

    # Calculate the total points scored by the Hornets in the remaining 40 seconds
    hornets_points = 2 * 2  # 2 two-point baskets

    # Calculate the final score and the difference in points
    fireflies_score = 86 + fireflies_points  # final score of the Fireflies
    hornets_score = 74 + hornets_points  # final score of the Hornets
    points_difference = fireflies_score - hornets_score

    result = points_difference
    return result

print(solution())