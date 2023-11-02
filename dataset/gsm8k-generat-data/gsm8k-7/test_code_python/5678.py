def solution():
    total_cars = 71 - 2  # subtracting the engine and caboose
    num_cargo_cars = (total_cars - 1) / 3  # subtracting one for the engine
    num_passenger_cars = total_cars - num_cargo_cars
    result = num_passenger_cars
    return result

print(solution())