def solution():
    # Define the number of planks for legs and surface per table
    legs_per_table = 4
    surface_per_table = 5

    # Calculate the total number of planks needed for 5 tables
    total_legs = legs_per_table * 5
    total_surface = surface_per_table * 5
    total_planks = total_legs + total_surface

    result = total_planks
    return result

print(solution())