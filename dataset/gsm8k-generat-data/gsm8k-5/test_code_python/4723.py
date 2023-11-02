def solution():
    distance_to_store = 1.5  # Cary walks 1.5 miles to the store and 1.5 miles home
    calories_burned_per_mile = 150  # Cary burns 150 calories per mile walked
    candy_bar_calories = 200  # Cary eats a candy bar with 200 calories

    # Calculate the total calories burned on the walk
    total_calories_burned = distance_to_store * 2 * calories_burned_per_mile

    # Calculate the net calorie deficit
    net_calorie_deficit = total_calories_burned - candy_bar_calories
    result = abs(net_calorie_deficit)  # Express result as a positive number
    return result

print(solution())