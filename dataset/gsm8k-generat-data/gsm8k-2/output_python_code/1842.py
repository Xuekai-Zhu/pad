def solution():
    """Darlene's car gets 20 miles/gallon. Martha's car gets half as many miles per gallon as Darlene’s car. How many gallons does Martha’s car require to make a 300-mile trip?"""
    darlene_mpg = 20
    martha_mpg = darlene_mpg / 2
    distance = 300
    gallons_needed = distance / martha_mpg
    result = gallons_needed
    return result

print(solution())