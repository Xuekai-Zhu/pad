def solution():
    # Calculate the total calories consumed from the candy bar
    candy_calories = 200

    # Calculate the total distance Cary walked
    total_distance = 3

    # Calculate the calories burned from walking
    calories_burned = 150 * total_distance

    # Calculate the net calorie deficit
    net_calorie_deficit = calories_burned - candy_calories
    result = abs(net_calorie_deficit)
    return result

print(solution())