def solution():
    """Cary walks 3 miles round-trip to the grocery store, where he buys and eats a candy bar with 200 calories. If Cary burns 150 calories per mile walked, what's Cary's net calorie deficit (expressed as a positive number)?"""
    # Define the distance Cary walks and the number of calories burned per mile
    DISTANCE = 3
    CALORIES_PER_MILE = 150

    # Calculate the number of calories burned during the walk
    calories_burned = DISTANCE * CALORIES_PER_MILE

    # Subtract the calories consumed from the calories burned
    net_calorie_deficit = calories_burned - 200

    # Take the absolute value of the net calorie deficit to express it as a positive number
    net_calorie_deficit = abs(net_calorie_deficit)

    # Display the net calorie deficit
    result = net_calorie_deficit
    return result

print(solution())