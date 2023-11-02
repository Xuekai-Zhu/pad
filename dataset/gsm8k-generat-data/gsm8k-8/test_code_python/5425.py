def solution():
    # Calculate the total carbon emissions from individual cars
    car_emissions = 80 * 10

    # Calculate the current carbon emissions from the bus
    bus_emissions = 100

    # Calculate the new number of people who drive after 25% start taking the bus
    new_car_population = 0.75 * 80

    # Calculate the new number of people who take the bus
    new_bus_population = 80 * 0.25

    # Calculate the new carbon emissions from individual cars
    new_car_emissions = new_car_population * 10

    # Calculate the new carbon emissions from the bus
    new_bus_emissions = (new_bus_population / 40) * 100

    # Calculate the total carbon emissions after the change
    new_total_emissions = new_car_emissions + new_bus_emissions

    # Calculate the reduction in carbon emissions
    reduction = car_emissions + bus_emissions - new_total_emissions

    result = reduction
    return result

print(solution())