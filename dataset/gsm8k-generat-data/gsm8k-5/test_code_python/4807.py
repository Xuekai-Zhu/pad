def solution():
    touchdown_points = 7  # Each touchdown is worth 7 points
    brayden_gavin_score = 7 * touchdown_points  # Brayden and Gavin scored 7 touchdowns
    cole_freddy_score = 9 * touchdown_points  # Cole and Freddy's team scored 9 touchdowns

    # Calculate the difference in scores
    score_difference = cole_freddy_score - brayden_gavin_score
    result = score_difference
    return result

print(solution())