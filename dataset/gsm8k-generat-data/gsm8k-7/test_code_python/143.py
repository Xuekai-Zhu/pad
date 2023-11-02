def solution():
    total_goldfish = 15
    surface_goldfish_percentage = 0.25

    # Calculate the number of goldfish at the surface
    surface_goldfish = total_goldfish * surface_goldfish_percentage

    # Calculate the number of goldfish below the surface
    below_surface_goldfish = total_goldfish - surface_goldfish
    result = below_surface_goldfish
    return result

print(solution())