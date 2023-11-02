def solution():
    # Calculate the height of the bone meal plant
    bone_meal_height = 36 * 1.25  # the bone meal plant grows to 125% of the height of the control plant

    # Calculate the height of the cow manure plant
    cow_manure_height = bone_meal_height * 2  # the cow manure plant grows to 200% of the height of the bone meal plant

    result = cow_manure_height
    return result

print(solution())