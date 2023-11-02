def solution():
    """Jim is wondering how many miles each gallon of gas gets him. His gas tank is 12 gallons. He has 2/3 of a tank left after he drives to and from work, which is 10 miles away from his house. How many miles per gallon does he get?"""
    gas_tank_size = 12
    gas_left = gas_tank_size * (2/3)
    round_trip_distance = 10 * 2
    miles_per_gallon = gas_left / round_trip_distance
    result = miles_per_gallon
    return result

print(solution())