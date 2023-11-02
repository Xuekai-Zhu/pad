def solution():
    lettuce_calories = 30  # Lettuce has 30 calories
    cucumber_calories = 80  # Cucumber has 80 calories
    crouton_calories = 20  # Each crouton has 20 calories
    crouton_count = 12  # There are 12 croutons in the salad

    # Calculate the total calories in the salad
    total_calories = lettuce_calories + cucumber_calories + (crouton_calories * crouton_count)
    result = total_calories
    return result

print(solution())