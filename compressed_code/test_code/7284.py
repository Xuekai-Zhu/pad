def solution():
    
    total_streetlights = 200
    parks_with_new_lights = 15
    streetlights_per_park = 12
    streetlights_used = parks_with_new_lights * streetlights_per_park
    streetlights_unused = total_streetlights - streetlights_used
    result = streetlights_unused
    return result

print(solution())