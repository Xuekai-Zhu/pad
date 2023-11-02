def solution():
    """Cary walks 3 miles round-trip to the grocery store, where he buys and eats a candy bar with 200 calories. If Cary burns 150 calories per mile walked, what's Cary's net calorie deficit (expressed as a positive number)?"""
    # Define the number of miles Cary walked and the number of calories he burned
    miles_walked = 3
    calories_burned = miles_walked * 2 * 150

    # Define the number of calories Cary consumed
    calories_consumed = 200

    # Calculate Cary's net calorie deficit
    net_calorie_deficit = calories_burned - calories_consumed

    # Return the result as a positive number
    result = abs(net_calorie_deficit)
    return result

print(solution())