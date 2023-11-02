def solution():
    dozen_in_recipe = 16
    butter_in_recipe = 4
    dozen_wanted = 4

    # Calculate the proportion of recipe needed for the desired amount of cookies
    proportion = dozen_wanted / dozen_in_recipe

    # Calculate the amount of butter needed for the desired amount of cookies
    butter_needed = proportion * butter_in_recipe

    result = butter_needed
    return result

print(solution())