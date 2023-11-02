def solution():
    cake_slices = 8  # The cake has 8 slices
    cake_calories_per_slice = 347  # Each slice of cake contains 347 calories
    brownie_slices = 6  # The pan of brownies has 6 slices
    brownie_calories_per_slice = 375  # Each brownie slice contains 375 calories

    # Calculate the total calories in the cake
    total_cake_calories = cake_slices * cake_calories_per_slice

    # Calculate the total calories in the brownies
    total_brownie_calories = brownie_slices * brownie_calories_per_slice

    # Calculate the difference in calories between the two desserts
    calories_diff = total_cake_calories - total_brownie_calories
    result = calories_diff
    return result

print(solution())