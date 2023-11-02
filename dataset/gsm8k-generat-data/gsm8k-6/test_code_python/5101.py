def solution():
    # Calculate the total number of planks of wood required to build 5 tables
    legs_planks = 5*4  # Each table needs 4 planks of wood for its legs
    surface_planks = 5*5  # Each table needs 5 planks of wood for its surface
    total_planks = legs_planks + surface_planks  # Total number of planks of wood required to build one table
    total_planks *= 5  # Total number of planks of wood required to build 5 tables
    result = total_planks
    return result

print(solution())