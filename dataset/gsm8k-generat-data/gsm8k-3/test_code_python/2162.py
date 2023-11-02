def solution():
    """On a weekend road trip, the Jensen family drove 210 miles on highways, where their car gets 35 miles for each gallon of gas and 54 miles on city streets where their car gets 18 miles for each gallon. How many gallons of gas did they use?"""
    # Define the number of miles driven on highways and city streets
    highway_miles = 210
    city_miles = 54

    # Define the miles per gallon for the car on highways and city streets
    highway_mpg = 35
    city_mpg = 18

    # Calculate the total gallons of gas used
    total_gallons = (highway_miles / highway_mpg) + (city_miles / city_mpg)

    # Display the total gallons of gas used
    result = total_gallons
    return result

print(solution())