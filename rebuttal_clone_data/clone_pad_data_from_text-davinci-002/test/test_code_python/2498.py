def solution():
    number_of_neighborhoods = 10
    number_of_roads = 4
    number_of_street_lights = 250
    total_number_of_street_lights = number_of_neighborhoods * number_of_roads * (2 * number_of_street_lights)
    result = total_number_of_street_lights
    return result

print(solution())