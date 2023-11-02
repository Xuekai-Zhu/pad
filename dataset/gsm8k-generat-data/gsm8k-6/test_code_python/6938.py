def solution():
    # Calculate the total number of cars in the train
    total_cars = 6 + 12 + 2  

    # Calculate the number of stations the train needs to pass to deliver all the cars
    coal_cars = 6  # initial number of coal cars
    iron_cars = 12  # initial number of iron cars
    wood_cars = 2  # initial number of wood cars
    stations = 0  # initial number of stations passed
    while coal_cars > 0 or iron_cars > 0 or wood_cars > 0:
        stations += 1
        coal_cars_left = max(coal_cars - 2, 0)
        iron_cars_left = max(iron_cars - 3, 0)
        wood_cars_left = max(wood_cars - 1, 0)
        coal_cars_deposited = coal_cars - coal_cars_left
        iron_cars_deposited = iron_cars - iron_cars_left
        wood_cars_deposited = wood_cars - wood_cars_left
        coal_cars = coal_cars_left + coal_cars_deposited
        iron_cars = iron_cars_left + iron_cars_deposited
        wood_cars = wood_cars_left + wood_cars_deposited

    # Calculate the total time in minutes the train needs to deliver all the cars
    time = stations * 25
    result = time
    return result

print(solution())