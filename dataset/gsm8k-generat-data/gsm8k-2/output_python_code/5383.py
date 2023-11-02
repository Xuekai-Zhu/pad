def solution():
    """An apple tree produced 200 apples in a particular season. The tree made 20% fewer fruits the following season, but the tree fruits production in the second season doubled during the third season. Calculate the total number of fruits the apple tree grew in the three seasons."""
    first_season_fruits = 200
    second_season_fruits = first_season_fruits * 0.8
    third_season_fruits = second_season_fruits * 2
    total_fruits = first_season_fruits + second_season_fruits + third_season_fruits
    result = total_fruits
    return result

print(solution())