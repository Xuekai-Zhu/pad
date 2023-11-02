def solution():
    taxi_capable_of_travel_over_water = False
    tokyo_location = "Japan"
    metropolitan_museum_location = "United States"
    separated_by_pacific_ocean = True
    if tokyo_location == metropolitan_museum_location and not separated_by_pacific_ocean or taxi_capable_of_travel_over_water:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())