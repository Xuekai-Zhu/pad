def solution():
    legs_per_table = 4  # each table has 4 legs
    surface_per_table = 5  # each table needs 5 planks for the surface
    num_tables = 5

    # Calculate the total number of planks needed for the legs for all tables
    total_legs_planks = num_tables * legs_per_table

    # Calculate the total number of planks needed for the surface for all tables
    total_surface_planks = num_tables * surface_per_table

    # Calculate the total number of planks needed for all tables
    total_planks = total_legs_planks + total_surface_planks
    result = total_planks
    return result

print(solution())