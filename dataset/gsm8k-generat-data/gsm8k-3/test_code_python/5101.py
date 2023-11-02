def solution():
    """Johnny is buying planks of wood to build some tables. Each table needs a plank of wood for each of the legs and 5 planks of wood for the surface. If Johnny wants to build 5 tables, how many planks of wood does he need?"""
    # Define the number of planks of wood needed per table
    LEG_PLANKS = 4
    SURFACE_PLANKS = 5

    # Define the number of tables Johnny wants to build
    num_tables = 5

    # Calculate the total number of planks of wood needed
    total_planks = LEG_PLANKS * num_tables + SURFACE_PLANKS * num_tables

    # Display the total number of planks of wood needed
    result = total_planks
    return result

print(solution())