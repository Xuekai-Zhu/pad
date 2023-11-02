def solution():
    """Darlene's car gets 20 miles/gallon. Martha's car gets half as many miles per gallon as Darlene’s car. How many gallons does Martha’s car require to make a 300-mile trip?"""
    # Define the miles per gallon of Darlene's car and calculate the miles per gallon of Martha's car
    darlene_mpg = 20
    martha_mpg = darlene_mpg / 2

    # Calculate the gallons of gas required for Martha's car to make a 300-mile trip
    gallons = 300 / martha_mpg

    # return the result rounded to two decimal places
    result = round(gallons, 2)
    return result

print(solution())