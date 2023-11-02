def solution():
    total_distance = 220  # Carol needs to drive 220 miles to get to college
    miles_per_gallon = 20  # Carol's car travels 20 miles per gallon
    gas_tank_size = 16  # Carol's car has a 16-gallon gas tank

    # Calculate how many gallons of gas Carol needs to make the trip
    gallons_needed = total_distance / miles_per_gallon

    # Calculate how many gallons of gas Carol has left when she arrives home
    gas_left = gas_tank_size - gallons_needed

    # Calculate how many more miles Carol can drive with the gas left in her tank
    extra_miles = gas_left * miles_per_gallon
    result = extra_miles
    return result

print(solution())