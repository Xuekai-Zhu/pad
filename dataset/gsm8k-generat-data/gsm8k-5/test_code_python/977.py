def solution():
    # Calculate the total number of wheels seen on trucks
    wheels_on_trucks = 12 * 4  # Each truck has 4 wheels

    # Calculate the total number of wheels seen on cars
    wheels_on_cars = 13 * 4  # Each car has 4 wheels

    # Add the number of wheels seen on all vehicles
    total_wheels = wheels_on_trucks + wheels_on_cars
    result = total_wheels
    return result

print(solution())