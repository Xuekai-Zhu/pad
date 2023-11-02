def solution():
    """Pria bought a new car that advertised an estimated gas mileage of 35 miles per gallon. The car has a 12-gallon tank. She filled her car full of gas and was able to drive a total of 372 miles. What was the difference, in miles per gallon, between Pria's mileage and the advertised mileage?"""
    tank_size = 12
    advertised_mpg = 35
    total_miles = 372
    actual_mpg = total_miles / tank_size
    difference = advertised_mpg - actual_mpg
    result = difference
    return result

print(solution())