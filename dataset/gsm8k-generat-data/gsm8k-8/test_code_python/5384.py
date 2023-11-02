def solution():
    # Calculate the number of apples produced in the second season
    second_season = 0.8 * 200
    # Calculate the number of apples produced in the third season
    third_season = 2 * second_season
    # Calculate the total number of apples produced in all three seasons
    total_apples = 200 + second_season + third_season
    result = total_apples
    return result

print(solution())