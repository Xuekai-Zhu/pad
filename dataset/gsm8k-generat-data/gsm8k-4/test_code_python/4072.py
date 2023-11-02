def solution():
    """A cake has 8 slices and each slice contains 347 calories. A pan of brownies has 6 brownies and each slice contains 375 calories. How many more calories does the cake have?"""
    # Define the number of slices in the cake and the number of brownies in the pan
    cake_slices = 8
    brownie_slices = 6

    # Define the number of calories in each cake slice and brownie slice
    cake_calories = 347
    brownie_calories = 375

    # Calculate the total number of calories in the cake and the pan of brownies
    total_cake_calories = cake_slices * cake_calories
    total_brownie_calories = brownie_slices * brownie_calories

    # Calculate the difference in calories between the cake and the pan of brownies
    calorie_difference = total_cake_calories - total_brownie_calories

    # Return the calorie difference
    result = calorie_difference
    return result

print(solution())