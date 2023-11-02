def solution():
    """Pria bought a new car that advertised an estimated gas mileage of 35 miles per gallon. The car has a 12-gallon tank. She filled her car full of gas and was able to drive a total of 372 miles. What was the difference, in miles per gallon, between Pria's mileage and the advertised mileage?"""
    gas_mileage = 35
    tank_size = 12
    total_distance = 372
    actual_mileage = total_distance / tank_size
    difference = gas_mileage - actual_mileage
    result = difference
    return result

print(solution())