def solution():
    # Calculate the total calories from the lettuce and cucumber
    lettuce_calories = 30
    cucumber_calories = 80
    total_veggie_calories = lettuce_calories + cucumber_calories

    # Calculate the total calories from the croutons
    crouton_calories = 20
    num_croutons = 12
    total_crouton_calories = crouton_calories * num_croutons

    # Calculate the total calories in the salad
    total_calories = total_veggie_calories + total_crouton_calories
    result = total_calories
    return result

print(solution())