def solution():
    planks_per_leg = 1  # Each table needs 1 plank of wood for each leg
    planks_per_surface = 5  # Each table needs 5 planks of wood for the surface
    tables = 5  # Johnny wants to build 5 tables

    # Calculate the total number of planks of wood Johnny needs
    total_planks = (planks_per_leg * 4 + planks_per_surface) * tables

    result = total_planks
    return result

print(solution())