def solution():
    neighborhoods = 10  # The town has 10 neighborhoods
    roads_per_neighborhood = 4  # Each neighborhood has 4 roads passing through it
    street_lights_per_road = 250 * 2  # Each road has 250 street lights on each opposite side

    # Calculate the total number of street lights in the town
    total_street_lights = neighborhoods * roads_per_neighborhood * street_lights_per_road
    result = total_street_lights
    return result

print(solution())