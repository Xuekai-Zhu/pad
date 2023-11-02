def solution():
    # Calculate the total number of wheels in the garage
    wheels_bicycles = 20 * 2  # each bicycle has 2 wheels
    wheels_cars = 10 * 4  # each car has 4 wheels
    wheels_motorcycles = 5 * 2  # each motorcycle has 2 wheels
    total_wheels = wheels_bicycles + wheels_cars + wheels_motorcycles  # sum of wheels of all vehicles
    result = total_wheels
    return result

print(solution())