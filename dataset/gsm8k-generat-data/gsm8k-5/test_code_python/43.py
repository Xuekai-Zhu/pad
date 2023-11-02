def solution():
    first_earthquake = 4  # The first earthquake caused 4 buildings to collapse
    total_buildings = first_earthquake
    for i in range(3):
        collapsed_buildings = 2 * total_buildings  # Each following earthquake has double the number of collapsing buildings
        total_buildings += collapsed_buildings  # Add the collapsed buildings from each earthquake to the total
    result = total_buildings
    return result

print(solution())