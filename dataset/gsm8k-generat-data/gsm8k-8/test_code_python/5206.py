def solution():
    # Define the height of the control plant
    control_height = 36

    # Calculate the height of the bone meal plant
    bone_meal_height = control_height * 1.25

    # Calculate the height of the cow manure plant
    cow_manure_height = bone_meal_height * 2

    result = cow_manure_height
    return result

print(solution())