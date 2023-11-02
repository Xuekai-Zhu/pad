def solution():
    num_neighborhoods = 10
    num_roads_per_neighborhood = 4
    num_street_lights_per_road = 250

    # Calculate the total number of roads in the town
    total_roads = num_neighborhoods * num_roads_per_neighborhood

    # Calculate the total number of street lights in the town
    total_street_lights = total_roads * num_street_lights_per_road * 2
    # multiply by 2 because we count both sides of the road
    result = total_street_lights
    return result

print(solution())