def solution():
    """On a weekend road trip, the Jensen family drove 210 miles on highways, where their car gets 35 miles for each gallon of gas and 54 miles on city streets where their car gets 18 miles for each gallon. How many gallons of gas did they use?"""
    # Define the distance driven on highways and city streets
    highway_distance = 210
    city_distance = 54

    # Define the car's fuel efficiency in miles per gallon on highways and city streets
    highway_efficiency = 35
    city_efficiency = 18

    # Calculate the number of gallons used on highways and city streets
    highway_gallons = highway_distance / highway_efficiency
    city_gallons = city_distance / city_efficiency

    # Calculate the total number of gallons used
    total_gallons = highway_gallons + city_gallons

    # Return the result
    result = total_gallons
    return result

print(solution())