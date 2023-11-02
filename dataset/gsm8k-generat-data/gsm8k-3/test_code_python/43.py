def solution():
    """An earthquake caused four buildings to collapse. Experts predicted that each following earthquake would have double the number of collapsing buildings as the previous one, since each one would make the foundations less stable. After three more earthquakes, how many buildings had collapsed including those from the first earthquake?"""
    # Define the number of buildings that collapsed in the first earthquake
    first_earthquake = 4

    # Initialize the total number of collapsed buildings
    total_buildings = 4

    # Loop through the next three earthquakes and double the number of collapsed buildings each time
    for i in range(3):
        collapsed_buildings = first_earthquake * (2**(i+1))
        total_buildings += collapsed_buildings

    # Return the total number of collapsed buildings
    result = total_buildings
    return result

print(solution())