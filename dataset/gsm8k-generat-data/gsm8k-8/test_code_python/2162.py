def solution():
    # Calculate the number of gallons used on highways
    highway_gallons = 210 / 35

    # Calculate the number of gallons used on city streets
    city_gallons = 54 / 18

    # Calculate the total number of gallons used
    total_gallons = highway_gallons + city_gallons

    result = total_gallons
    return result

print(solution())