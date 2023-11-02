def solution():
    """In Johnstown, the population is 80 and every single person drives by themselves to work. Each car on a road pollutes 10 pounds of carbon a year. A single bus pollutes 100 pounds of carbon a year. A bus can hold 40 people. The town decides to start running a bus and 25% of the people who used to drive now take the bus. How many fewer pounds of carbon are now emitted per year?"""
    # Define the population and the polluting factor of a car and a bus
    population = 80
    car_polluting_factor = 10
    bus_polluting_factor = 100
    bus_capacity = 40

    # Calculate the total amount of pollution before the bus is introduced
    total_pollution_before = population * car_polluting_factor

    # Calculate the number of people who will take the bus
    bus_passengers = int(population * 0.25)

    # Calculate the number of cars still on the road
    cars_on_road = population - bus_passengers

    # Calculate the new total amount of pollution with the bus
    total_pollution_after = (cars_on_road * car_polluting_factor) + ((population - cars_on_road) // bus_capacity * bus_polluting_factor)

    # Calculate the difference in pollution
    pollution_difference = total_pollution_before - total_pollution_after

    # Return the result
    result = pollution_difference
    return result

print(solution())