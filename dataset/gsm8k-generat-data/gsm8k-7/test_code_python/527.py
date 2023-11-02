def solution():
    lettuce_calories = 30
    cucumber_calories = 80
    crouton_calories = 20

    num_croutons = 12

    # Calculate the total number of calories from the croutons
    total_crouton_calories = num_croutons * crouton_calories

    # Calculate the total number of calories from the lettuce and cucumber
    total_veggie_calories = lettuce_calories + cucumber_calories

    # Calculate the total number of calories in the salad
    total_calories = total_veggie_calories + total_crouton_calories
    result = total_calories
    return result

print(solution())