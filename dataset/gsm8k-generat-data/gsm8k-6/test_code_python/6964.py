def solution():
    # Calculate the total number of calories in the Cheezits
    total_cheezit_calories = 3 * 2 * 150  # 3 bags, 2 ounces each, 150 calories per ounce

    # Calculate the number of calories burned during the run
    calories_burned = 12 * 40  # 12 calories burned per minute, 40 minutes

    # Calculate the excess calories eaten by James
    excess_calories = total_cheezit_calories - calories_burned
    result = excess_calories
    return result

print(solution())