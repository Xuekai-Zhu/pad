def solution():
    first_season_fruits = 200
    second_season_fruits = first_season_fruits - (first_season_fruits * 0.2)  # 20% fewer fruits in the second season
    third_season_fruits = second_season_fruits * 2  # double the fruits in the third season

    total_fruits = first_season_fruits + second_season_fruits + third_season_fruits
    result = total_fruits
    return result

print(solution())