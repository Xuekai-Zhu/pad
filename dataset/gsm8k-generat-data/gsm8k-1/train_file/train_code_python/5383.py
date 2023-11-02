def solution():
    """An apple tree produced 200 apples in a particular season. The tree made 20% fewer fruits the following season, but the tree fruits production in the second season doubled during the third season. Calculate the total number of fruits the apple tree grew in the three seasons."""
    first_season = 200
    second_season = first_season * 0.8
    third_season = second_season * 2
    total_fruits = first_season + second_season + third_season
    result = total_fruits
    return result

print(solution())