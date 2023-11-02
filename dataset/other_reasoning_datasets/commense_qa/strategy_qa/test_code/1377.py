def solution():
    # Define the location of South Africa and Cape Town
    south_africa_location = "south of the Equator"
    cape_town_location = south_africa_location
    # Check if Cape Town is south of the Equator
    if cape_town_location == south_africa_location:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())