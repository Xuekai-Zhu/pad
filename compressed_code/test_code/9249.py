def solution():
    
    neighborhoods = 10
    roads_per_neighborhood = 4
    lights_per_road = 250 * 2
    total_lights = neighborhoods * roads_per_neighborhood * lights_per_road
    result = total_lights
    return result

print(solution())