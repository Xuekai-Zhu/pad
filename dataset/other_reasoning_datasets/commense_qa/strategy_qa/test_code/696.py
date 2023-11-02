def solution():
    # Define the characteristics of symbolic and anatomical hearts
    symbolic_heart_shape = "sharply pointed at bottom with valley between bumps at top"
    anatomical_heart_shape = "rounded with numerous vascular tubes entering and exiting"
    # Check if the two heart types have significantly different shapes
    if symbolic_heart_shape != anatomical_heart_shape:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())