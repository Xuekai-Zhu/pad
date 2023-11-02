def solution():
    airport_location = "Orange County"
    nearby_residential_areas = True
    noise_ordinance = True
    commercial_pilots = True
    if airport_location == "Orange County" and nearby_residential_areas and noise_ordinance and not commercial_pilots:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())