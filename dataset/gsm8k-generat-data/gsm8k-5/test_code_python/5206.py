def solution():
    control_plant = 36  # Control plant grows 36 inches high
    bone_meal_plant = 1.25 * control_plant  # Bone meal plant grows to 125% of control plant height
    cow_manure_plant = 2 * bone_meal_plant  # Cow manure plant grows to 200% of bone meal plant height

    # Calculate the height of the cow manure plant
    height_cow_manure = cow_manure_plant
    result = height_cow_manure
    return result

print(solution())