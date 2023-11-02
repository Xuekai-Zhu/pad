def solution():
    """On a weekend road trip, the Jensen family drove 210 miles on highways, where their car gets 35 miles for each gallon of gas and 54 miles on city streets where their car gets 18 miles for each gallon. How many gallons of gas did they use?"""
    highway_miles = 210
    city_miles = 54
    highway_mpg = 35
    city_mpg = 18
    highway_gallons = highway_miles / highway_mpg
    city_gallons = city_miles / city_mpg
    total_gallons = highway_gallons + city_gallons
    result = total_gallons
    return result

print(solution())