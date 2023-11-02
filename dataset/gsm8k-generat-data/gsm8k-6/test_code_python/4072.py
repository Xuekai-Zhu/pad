def solution():
    # Calculate the total number of calories in the cake and the pan of brownies
    calories_cake = 8 * 347  # 8 slices, each containing 347 calories
    calories_brownies = 6 * 375  # 6 brownies, each containing 375 calories

    # Calculate the difference in calories between the cake and the pan of brownies
    calorie_difference = calories_cake - calories_brownies
    result = calorie_difference
    return result

print(solution())