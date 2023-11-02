def solution():
    """A town has ten neighborhoods, each having four roads passing through them. Each of the roads has 250 street lights on each opposite side. Calculate the total number of street lights on all the roads of the neighborhoods in the town."""
    neighborhoods = 10
    roads_per_neighborhood = 4
    lights_per_road = 250 * 2
    total_lights = neighborhoods * roads_per_neighborhood * lights_per_road
    result = total_lights
    return result

print(solution())