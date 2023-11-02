def solution():
    """Darlene's car gets 20 miles/gallon. Martha's car gets half as many miles per gallon as Darlene’s car. How many gallons does Martha’s car require to make a 300-mile trip?"""
    # Define Darlene's car mileage and calculate Martha's car mileage
    DARLENE_MILEAGE = 20
    MARTHA_MILEAGE = DARLENE_MILEAGE / 2

    # Define the distance of the trip
    distance = 300

    # Calculate the number of gallons Martha's car will require
    gallons = distance / MARTHA_MILEAGE

    # Display the result
    result = gallons
    return result

print(solution())