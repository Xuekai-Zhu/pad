def solution():
    """Pria bought a new car that advertised an estimated gas mileage of 35 miles per gallon. The car has a 12-gallon tank. She filled her car full of gas and was able to drive a total of 372 miles. What was the difference, in miles per gallon, between Pria's mileage and the advertised mileage?"""
    # Define the advertised mileage and the tank capacity
    ADVERTISED_MILEAGE = 35
    TANK_CAPACITY = 12

    # Calculate the total distance traveled and the actual mileage
    total_distance = 372
    actual_mileage = total_distance / TANK_CAPACITY

    # Calculate the difference between the actual and advertised mileage
    mileage_difference = ADVERTISED_MILEAGE - actual_mileage

    # return the result
    result = mileage_difference
    return result

print(solution())