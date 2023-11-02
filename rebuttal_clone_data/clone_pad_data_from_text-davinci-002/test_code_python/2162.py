def solution():
    total_miles = 210
    highway_miles = 35
    city_miles = 54
    highway_gallons = total_miles / highway_miles
    city_gallons = total_miles / city_miles
    total_gallons = highway_gallons + city_gallons
    result = total_gallons
    return result

print(solution())