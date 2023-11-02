def solution():
    """An earthquake caused four buildings to collapse. Experts predicted that each following earthquake would have double the number of collapsing buildings as the previous one, since each one would make the foundations less stable. After three more earthquakes, how many buildings had collapsed including those from the first earthquake?"""
    # Define the initial number of collapsed buildings
    collapsed_buildings = 4

    # Calculate the number of collapsed buildings after each subsequent earthquake
    for i in range(3):
        collapsed_buildings *= 2

    # Add the number of buildings collapsed from the first earthquake
    total_buildings_collapsed = collapsed_buildings + 4

    # return the result
    result = total_buildings_collapsed
    return result

print(solution())