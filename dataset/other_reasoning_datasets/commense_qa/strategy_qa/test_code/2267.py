def solution():
    maximum_height_clearance = 13
    oasis_cruise_boat_height = 236
    if oasis_cruise_boat_height > maximum_height_clearance:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())