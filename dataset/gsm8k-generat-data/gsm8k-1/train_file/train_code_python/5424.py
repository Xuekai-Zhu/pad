def solution():
    """In Johnstown, the population is 80 and every single person drives by themselves to work. Each car on a road pollutes 10 pounds of carbon a year. A single bus pollutes 100 pounds of carbon a year. A bus can hold 40 people. The town decides to start running a bus and 25% of the people who used to drive now take the bus. How many fewer pounds of carbon are now emitted per year?"""
    population = 80
    cars = population
    car_emissions = 10
    bus_emissions = 100
    bus_capacity = 40
    bus_riders = round(population * 0.25)
    car_drivers = population - bus_riders
    total_car_emissions = car_drivers * car_emissions
    total_bus_emissions = bus_emissions if bus_riders == 0 else bus_emissions * (1 + (bus_riders // bus_capacity))
    total_emissions = total_car_emissions + total_bus_emissions
    num_people_affected_by_bus = bus_riders
    emissions_offset = (car_emissions - bus_emissions) * num_people_affected_by_bus
    result = total_emissions - emissions_offset
    return result

print(solution())