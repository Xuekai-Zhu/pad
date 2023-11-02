def solution():
    """Pria bought a new car that advertised an estimated gas mileage of 35 miles per gallon. The car has a 12-gallon tank. She filled her car full of gas and was able to drive a total of 372 miles. What was the difference, in miles per gallon, between Pria's mileage and the advertised mileage?"""
    # Define the advertised gas mileage and the tank size
    ADVERTISED_MPG = 35
    TANK_SIZE = 12

    # Calculate the actual gas mileage
    actual_mpg = 372 / TANK_SIZE

    # Calculate the difference between the actual and advertised gas mileage
    mpg_difference = ADVERTISED_MPG - actual_mpg

    # Display the difference in miles per gallon
    result = mpg_difference
    return result

print(solution())