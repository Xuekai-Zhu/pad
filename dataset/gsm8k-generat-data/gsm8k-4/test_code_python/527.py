def solution():
    """Jason is making a salad. The lettuce has 30 calories, the cucumber has 80 calories, and the 12 croutons have 20 calories each. How many calories are in the salad?"""
    # Define the calorie counts for each ingredient
    lettuce_calories = 30
    cucumber_calories = 80
    crouton_calories = 20
    num_croutons = 12

    # Calculate the total calorie count of the salad
    total_calories = lettuce_calories + cucumber_calories + (crouton_calories * num_croutons)

    # Return the result
    result = total_calories
    return result

print(solution())