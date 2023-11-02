def solution():
    """Each pole on a road intersection has 4 street lights. If the number of poles at each intersection is 6, and the road has 4 intersections, calculate the total number of functioning street lights if 20 streetlights from the total number are not working."""
    poles_per_intersection = 6
    lights_per_pole = 4
    intersections = 4
    total_lights = poles_per_intersection * lights_per_pole * intersections
    working_lights = total_lights - 20
    result = working_lights
    return result

print(solution())