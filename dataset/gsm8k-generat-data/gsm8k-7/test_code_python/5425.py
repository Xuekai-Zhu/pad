def solution():
    population = 80
    car_pollution = 10
    bus_pollution = 100
    bus_capacity = 40
    bus_ridership = 0.25

    # Calculate the number of cars on the road
    num_cars = population

    # Calculate the total pollution from cars
    total_car_pollution = num_cars * car_pollution

    # Calculate the total pollution from the initial bus
    total_bus_pollution = bus_pollution

    # Calculate the number of people who will ride the bus
    num_bus_riders = int(population * bus_ridership)

    # Calculate the total pollution from the additional bus riders
    total_bus_rider_pollution = (num_bus_riders // bus_capacity + 1) * bus_pollution

    # Calculate the total pollution after the bus is introduced
    total_pollution = total_car_pollution - total_bus_pollution - total_bus_rider_pollution

    # Calculate the reduction in pollution
    pollution_reduction = total_car_pollution - total_pollution
    result = pollution_reduction
    return result

print(solution())