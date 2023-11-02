def solution():
    """Sophia is thinking of taking a road trip in her car, and would like to know how far she can drive on a single tank of gas. She has traveled 100 miles since last filling her tank, and she needed to put in 4 gallons of gas to fill it up again. The owner's manual for her car says that her tank holds 12 gallons of gas. How many miles can Sophia drive on a single tank of gas?"""
    miles_traveled = 100
    gallons_used = 4
    tank_size = 12
    miles_per_gallon = miles_traveled / gallons_used
    total_distance = miles_per_gallon * tank_size
    result = total_distance
    return result

print(solution())