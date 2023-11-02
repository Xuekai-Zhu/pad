def solution():
    """Johnny is buying planks of wood to build some tables. Each table needs a plank of wood for each of the legs and 5 planks of wood for the surface. If Johnny wants to build 5 tables, how many planks of wood does he need?"""
    legs_per_table = 4
    surface_per_table = 5
    tables = 5
    total_planks = (legs_per_table + surface_per_table) * tables
    result = total_planks
    return result

print(solution())