def solution():
    caracal_native_regions = ["Africa", "Middle East", "Central Asia", "India"]
    university_location = "United States"
    university_continent = "North America"
    if university_continent in caracal_native_regions:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())