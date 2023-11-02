def solution():
    """Matthew and his brother Shawn played swimming-pool-basketball. Each basket was worth 3 points. Matthew scored 9 points. Shawn scored 6 points. What is the total number of baskets made during this game?"""
    # Define the point value of each basket
    BASKET_VALUE = 3

    # Calculate the number of baskets Matthew made
    matthew_baskets = 9 // BASKET_VALUE

    # Calculate the number of baskets Shawn made
    shawn_baskets = 6 // BASKET_VALUE

    # Calculate the total number of baskets made during the game
    total_baskets = matthew_baskets + shawn_baskets

    result = total_baskets
    return result

print(solution())