def solution():
    """In Johnstown, the population is 80 and every single person drives by themselves to work. Each car on a road pollutes 10 pounds of carbon a year. A single bus pollutes 100 pounds of carbon a year. A bus can hold 40 people. The town decides to start running a bus and 25% of the people who used to drive now take the bus. How many fewer pounds of carbon are now emitted per year?"""
    population = 80
    car_pollution = 10
    bus_pollution = 100
    bus_capacity = 40
    total_car_pollution = population * car_pollution
    cars_on_the_road = population
    people_on_the_bus = population * 0.25
    remaining_cars = cars_on_the_road - people_on_the_bus
    total_pollution_with_bus = (total_car_pollution - (remaining_cars * car_pollution)) + (bus_pollution * 1)
    total_pollution_without_bus = total_car_pollution
    result = total_pollution_without_bus - total_pollution_with_bus
    return result

print(solution())