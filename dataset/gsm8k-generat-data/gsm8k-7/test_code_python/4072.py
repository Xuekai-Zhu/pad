def solution():
    num_slices_cake = 8
    calories_per_slice_cake = 347

    num_brownies = 6
    calories_per_brownie = 375

    # Calculate the total number of calories in the cake
    total_calories_cake = num_slices_cake * calories_per_slice_cake

    # Calculate the total number of calories in the brownies
    total_calories_brownies = num_brownies * calories_per_brownie

    # Calculate the difference in calories between the two desserts
    calorie_difference = total_calories_cake - total_calories_brownies
    result = calorie_difference
    return result

print(solution())