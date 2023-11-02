def solution():
    """In Johnstown, the population is 80 and every single person drives by themselves to work. Each car on a road pollutes 10 pounds of carbon a year. A single bus pollutes 100 pounds of carbon a year. A bus can hold 40 people. The town decides to start running a bus and 25% of the people who used to drive now take the bus. How many fewer pounds of carbon are now emitted per year?"""
    # Define the population and pollution data
    POPULATION = 80
    CAR_POLLUTION = 10
    BUS_POLLUTION = 100
    BUS_CAPACITY = 40

    # Calculate the initial pollution from cars
    initial_car_pollution = POPULATION * CAR_POLLUTION

    # Calculate the number of people who choose to take the bus
    bus_riders = POPULATION * 0.25
    remaining_drivers = POPULATION - bus_riders

    # Calculate the number of required buses
    required_buses = (bus_riders // BUS_CAPACITY) + 1

    # Calculate the total pollution from buses
    bus_pollution = required_buses * BUS_POLLUTION

    # Calculate the new total pollution
    new_total_pollution = initial_car_pollution - (bus_pollution + (remaining_drivers * CAR_POLLUTION))

    # Calculate the reduction in pollution
    pollution_reduction = initial_car_pollution - new_total_pollution

    # Display the reduction in pollution
    result = pollution_reduction
    return result

print(solution())