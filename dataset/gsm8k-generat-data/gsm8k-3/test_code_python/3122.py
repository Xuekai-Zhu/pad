def solution():
    """Matthew and his brother Shawn played swimming-pool-basketball. Each basket was worth 3 points. Matthew scored 9 points. Shawn scored 6 points. What is the total number of baskets made during this game?"""
    # Define the points per basket
    POINTS_PER_BASKET = 3

    # Calculate the number of baskets made by Matthew
    matthew_baskets = 9 / POINTS_PER_BASKET

    # Calculate the number of baskets made by Shawn
    shawn_baskets = 6 / POINTS_PER_BASKET

    # Calculate the total number of baskets made
    total_baskets = matthew_baskets + shawn_baskets

    # Display the total number of baskets made
    result = total_baskets
    return result

print(solution())