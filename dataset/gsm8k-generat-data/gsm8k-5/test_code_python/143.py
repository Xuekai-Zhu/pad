def solution():
    visible_goldfish = 15  # Toby counted 15 goldfish in total
    surface_goldfish_percentage = 0.25  # Toby knows that only 25% of goldfish are at the surface

    # Calculate the total number of goldfish
    total_goldfish = visible_goldfish / surface_goldfish_percentage

    # Calculate the number of goldfish that are below the surface
    below_surface_goldfish = total_goldfish - visible_goldfish
    result = below_surface_goldfish
    return result

print(solution())