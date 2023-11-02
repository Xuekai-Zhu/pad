def solution():
    distance_home = 220
    mpg = 20
    tank_size = 16

    # Calculate how many gallons of gas Carol will use to travel home
    gallons_used = distance_home / mpg

    # Calculate how many gallons of gas she will have left in her tank
    gallons_left = tank_size - gallons_used

    # Calculate how many miles she can drive with the remaining gas
    miles_left = gallons_left * mpg
    result = miles_left
    return result

print(solution())