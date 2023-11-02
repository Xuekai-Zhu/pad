def solution():
    """A cake has 8 slices and each slice contains 347 calories.  A pan of brownies has 6 brownies and each slice contains 375 calories.  How many more calories does the cake have?"""
    # Define the number of slices in the cake and the calories per slice
    CAKE_SLICES = 8
    CAKE_CALORIES_PER_SLICE = 347

    # Define the number of brownies in the pan and the calories per brownie
    BROWNIES = 6
    BROWNIE_CALORIES_PER_SLICE = 375

    # Calculate the total calories in the cake
    cake_calories = CAKE_SLICES * CAKE_CALORIES_PER_SLICE

    # Calculate the total calories in the pan of brownies
    brownie_calories = BROWNIES * BROWNIE_CALORIES_PER_SLICE

    # Calculate the difference in calories between the cake and the brownies
    calorie_difference = cake_calories - brownie_calories

    # Display the calorie difference
    result = calorie_difference
    return result

print(solution())