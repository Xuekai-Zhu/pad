def solution():
    # Define the number of calories per slice of cake and brownie
    cake_calories = 347
    brownie_calories = 375

    # Calculate the total number of calories in cake and brownies
    total_cake_calories = cake_calories * 8
    total_brownie_calories = brownie_calories * 6

    # Calculate the difference in calories between cake and brownies
    calorie_difference = total_cake_calories - total_brownie_calories
    result = calorie_difference
    return result

print(solution())