def solution():
    num_streetlights_per_intersection = 4
    num_intersection_poles = 6
    num_streetlights_not_working = 20

    # Calculate the total number of poles on the road
    total_poles = num_intersection_poles * num_streetlights_per_intersection

    # Calculate the total number of functioning street lights on the road
    total_functioning_lights = total_poles * num_streetlights_not_working
    result = total_functioning_lights
    return result

print(solution())