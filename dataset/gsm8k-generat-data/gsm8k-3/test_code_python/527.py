def solution():
    """Jason is making a salad. The lettuce has 30 calories, the cucumber has 80 calories, and the 12 croutons have 20 calories each. How many calories are in the salad?"""
    # Define the number of calories for each ingredient
    LETTUCE_CALORIES = 30
    CUCUMBER_CALORIES = 80
    CROUTON_CALORIES = 20

    # Define the number of each ingredient in the salad
    lettuce_count = 1
    cucumber_count = 1
    crouton_count = 12

    # Calculate the total number of calories in the salad
    total_calories = (lettuce_count * LETTUCE_CALORIES) + (cucumber_count * CUCUMBER_CALORIES) + (crouton_count * CROUTON_CALORIES)

    # Display the total number of calories
    result = total_calories
    return result

print(solution())