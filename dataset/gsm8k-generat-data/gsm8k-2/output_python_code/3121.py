def solution():
    """Matthew and his brother Shawn played swimming-pool-basketball. Each basket was worth 3 points. Matthew scored 9 points. Shawn scored 6 points. What is the total number of baskets made during this game?"""
    baskets_per_point = 1 / 3
    matthew_baskets = 9 * baskets_per_point
    shawn_baskets = 6 * baskets_per_point
    total_baskets = matthew_baskets + shawn_baskets
    result = total_baskets
    return result

print(solution())