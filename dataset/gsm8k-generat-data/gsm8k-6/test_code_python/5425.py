def solution():
    # Calculate the total amount of carbon emitted by cars before the bus is introduced
    carbon_cars = 80 * 10  # each person who drives emits 10 pounds of carbon a year

    # Calculate the amount of carbon emitted by the bus before any people switch to it
    carbon_bus = 100

    # Calculate the total amount of carbon emitted after 25% of the people start taking the bus
    new_population = 0.75 * 80  # 25% of the population is now taking the bus
    new_cars = new_population * 10  # the remaining people who drive emit 10 pounds of carbon each
    new_bus = carbon_bus if new_population > 40 else 0  # if the bus is full, it replaces all remaining cars

    # Calculate the total amount of carbon emitted after the switch to the bus
    total_carbon = new_cars + new_bus

    # Calculate the amount of carbon that is now emitted
    carbon_saved = carbon_cars - total_carbon
    result = carbon_saved
    return result

print(solution())