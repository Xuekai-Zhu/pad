def solution():
    
    neighborhoods = 10
    roads_per_neighborhood = 4
    street_lights_per_road = 250 * 2
    total_street_lights = neighborhoods * roads_per_neighborhood * street_lights_per_road
    result = total_street_lights
    return result

print(solution())