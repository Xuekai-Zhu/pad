def solution():
    """A car uses 20 gallons of gas to travel 400 miles. Mr. Montero's car has 8 gallons in it. How many more gallons of gas does he need to travel 600 miles, back and forth?"""
    # Calculate the number of gallons of gas needed per mile
    gas_per_mile = 20 / 400

    # Calculate the number of miles Mr. Montero's car can travel with 8 gallons
    miles_with_8_gallons = 8 / gas_per_mile

    # Calculate the number of additional miles Mr. Montero can travel
    additional_miles = 600 - (miles_with_8_gallons * 2)

    # Calculate the additional gallons of gas needed
    additional_gallons = additional_miles * gas_per_mile

    result = additional_gallons
    return result

print(solution())