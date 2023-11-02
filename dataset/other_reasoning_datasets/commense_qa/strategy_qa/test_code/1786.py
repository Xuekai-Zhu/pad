def solution():
    sea_shanties_on_sea_vessels = True
    oregon_trail_land_based = True
    if sea_shanties_on_sea_vessels and not oregon_trail_land_based:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())