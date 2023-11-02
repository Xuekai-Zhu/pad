def solution():
    # Define the number of neighborhoods and roads in each neighborhood
    num_neighborhoods = 10
    num_roads_per_neighborhood = 4

    # Define the number of street lights on each side of a road
    num_street_lights_per_side = 250

    # Calculate the total number of street lights on all roads in all neighborhoods
    total_street_lights = num_neighborhoods * num_roads_per_neighborhood * 2 * num_street_lights_per_side
    result = total_street_lights
    return result

print(solution())