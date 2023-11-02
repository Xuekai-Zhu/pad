def solution():
    """A town has ten neighborhoods, each having four roads passing through them. Each of the roads has 250 street lights on each opposite side. Calculate the total number of street lights on all the roads of the neighborhoods in the town."""
    # Define the number of neighborhoods and roads
    NUM_NEIGHBORHOODS = 10
    NUM_ROADS_PER_NEIGHBORHOOD = 4

    # Define the number of street lights per road
    NUM_STREET_LIGHTS_PER_ROAD = 250 * 2

    # Calculate the total number of street lights in the town
    total_street_lights = NUM_NEIGHBORHOODS * NUM_ROADS_PER_NEIGHBORHOOD * NUM_STREET_LIGHTS_PER_ROAD

    # return the result
    result = total_street_lights
    return result

print(solution())