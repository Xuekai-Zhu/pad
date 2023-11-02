def solution():
    """Johnny is buying planks of wood to build some tables. Each table needs a plank of wood for each of the legs and 5 planks of wood for the surface. If Johnny wants to build 5 tables, how many planks of wood does he need?"""
    # Define the number of tables Johnny wants to build
    num_tables = 5

    # Define the number of planks of wood needed for each table
    legs_per_table = 4
    surface_per_table = 5

    # Calculate the total number of planks of wood needed
    total_legs = num_tables * legs_per_table
    total_surface = num_tables * surface_per_table
    total_planks = total_legs + total_surface

    # Return the result
    result = total_planks
    return result

print(solution())