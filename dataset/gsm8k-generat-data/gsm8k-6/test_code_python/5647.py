def solution():
    # Calculate the number of gallons of gas needed for the trip
    gallons_used = 220 / 20 

    # Calculate the number of gallons left in the tank after the trip
    gallons_left = 16 - gallons_used  

    # Calculate the number of miles Carol can still drive with the remaining gas
    remaining_miles = gallons_left * 20 

    result = remaining_miles
    return result

print(solution())