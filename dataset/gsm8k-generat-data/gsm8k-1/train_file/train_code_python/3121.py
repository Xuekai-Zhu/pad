def solution():
    """Matthew and his brother Shawn played swimming-pool-basketball. Each basket was worth 3 points. Matthew scored 9 points. Shawn scored 6 points. What is the total number of baskets made during this game?"""
    matthew_score = 9
    shawn_score = 6
    points_per_basket = 3
    total_baskets = (matthew_score + shawn_score) // points_per_basket
    result = total_baskets
    return result

print(solution())