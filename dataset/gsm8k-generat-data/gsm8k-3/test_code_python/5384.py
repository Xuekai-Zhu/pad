def solution():
    """An apple tree produced 200 apples in a particular season. The tree made 20% fewer fruits the following season, but the tree fruits production in the second season doubled during the third season. Calculate the total number of fruits the apple tree grew in the three seasons."""
    # Define the number of apples in the first season
    season1 = 200

    # Calculate the number of apples in the second season, which is 20% fewer than the first season
    season2 = season1 * 0.8

    # Calculate the number of apples in the third season, which is double the number in the second season
    season3 = season2 * 2

    # Calculate the total number of apples produced in the three seasons
    total = season1 + season2 + season3

    # Display the total number of apples produced
    result = total
    return result

print(solution())