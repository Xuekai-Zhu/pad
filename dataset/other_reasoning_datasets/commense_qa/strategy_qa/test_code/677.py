def solution():
    federal_reserve_location = "Washington, D.C."
    space_needle_location = "Seattle, Washington"
    distance_in_miles = 2700
    if federal_reserve_location != space_needle_location and distance_in_miles > 2:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())