def solution():
    """Jenny wants to know whether bone meal or cow manure makes better fertilizer. The control plant with no fertilizer grows 36 inches high, the plant with bone meal grows to 125% of the height of the control plant, and the cow manure plant grows to 200% of the height of the bone meal plant. How tall is the cow manure plant in inches?"""
    # Define the height of the control plant and calculate the height of the bone meal plant
    control_height = 36
    bone_meal_height = control_height * 1.25

    # Calculate the height of the cow manure plant
    cow_manure_height = bone_meal_height * 2

    # Display the height of the cow manure plant
    result = cow_manure_height
    return result

print(solution())