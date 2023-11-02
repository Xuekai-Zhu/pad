def solution():
    """Cary walks 3 miles round-trip to the grocery store, where he buys and eats a candy bar with 200 calories. If Cary burns 150 calories per mile walked, what's Cary's net calorie deficit (expressed as a positive number)?"""
    miles_walked = 3
    calories_burned_per_mile = 150
    total_calories_burned = miles_walked * calories_burned_per_mile
    candy_bar_calories = 200
    net_calorie_deficit = total_calories_burned - candy_bar_calories
    result = abs(net_calorie_deficit)
    return result

print(solution())