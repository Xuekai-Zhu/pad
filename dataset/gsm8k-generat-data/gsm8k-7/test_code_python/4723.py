def solution():
    distance = 3  # round-trip in miles
    calories_per_mile = 150
    candy_bar_calories = 200

    # Calculate the total calories burned during the walk
    total_calories_burned = distance * calories_per_mile

    # Calculate the net calorie deficit
    net_calorie_deficit = total_calories_burned - candy_bar_calories
    result = net_calorie_deficit
    return result

print(solution())