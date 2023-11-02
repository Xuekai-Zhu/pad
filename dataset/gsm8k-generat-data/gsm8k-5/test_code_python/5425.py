def solution():
    # Calculate the total pounds of carbon emitted by cars
    car_emissions = 80 * 10  # Each person driving in their own car emits 10 pounds of carbon per year

    # Calculate the total pounds of carbon emitted by the bus
    bus_emissions = 0  # Initially, there was no bus
    if 20 in range(1, 80): # check that at least one person is taking the bus
        bus_emissions = (100 / 40) * 20  # 20 people now take the bus, each person counts as 2 people (one less car and one person on the bus)

    # Calculate the new total pounds of carbon emitted
    new_total_emissions = car_emissions - bus_emissions

    # Calculate the reduction in pounds of carbon emissions
    reduction = car_emissions - new_total_emissions
    result = reduction
    return result

print(solution())