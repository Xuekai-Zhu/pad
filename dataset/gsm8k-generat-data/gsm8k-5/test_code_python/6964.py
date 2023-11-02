def solution():
    # Calories consumed from Cheezits
    calories_cheezits = 3 * 2 * 150  # 3 bags, 2 ounces per bag, 150 calories per ounce

    # Calories burned from running
    calories_burned = 12 * 40  # 12 calories per minute, 40 minutes of running

    # Excess calories consumed
    excess_calories = calories_cheezits - calories_burned
    result = excess_calories
    return result

print(solution())