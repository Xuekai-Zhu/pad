def solution():
    # Calculate the total number of street lights in one neighborhood 
    street_lights_per_neighborhood = 4 * 250 * 2  # four roads per neighborhood, 250 street lights on each side of the road

    # Calculate the total number of street lights in all ten neighborhoods 
    total_street_lights = street_lights_per_neighborhood * 10

    result = total_street_lights
    return result

print(solution())