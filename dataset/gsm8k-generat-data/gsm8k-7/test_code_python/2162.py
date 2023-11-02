def solution():
    highway_miles = 210
    highway_mpg = 35
    city_miles = 54
    city_mpg = 18

    # Calculate the total gallons of gas used on the highway
    highway_gallons = highway_miles / highway_mpg

    # Calculate the total gallons of gas used in the city
    city_gallons = city_miles / city_mpg

    # Calculate the total gallons of gas used
    total_gallons = highway_gallons + city_gallons
    result = total_gallons
    return result

print(solution())