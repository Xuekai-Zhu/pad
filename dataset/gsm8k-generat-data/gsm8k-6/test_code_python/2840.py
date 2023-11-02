def solution():
    # Calculate the number of wheels contributed by cars
    car_wheels = 19 * 5

    # Calculate the number of motorcycles
    motorcycles = (117 - car_wheels) / 2
    result = motorcycles
    return result

print(solution())