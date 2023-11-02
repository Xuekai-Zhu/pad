def solution():
    """198 passengers fit into 9 buses. How many passengers fit in 5 buses?"""
    # Define the initial number of passengers and buses
    passengers = 198
    buses = 9

    # Calculate the average number of passengers per bus
    avg_passengers_per_bus = passengers / buses

    # Calculate the number of passengers that fit in 5 buses
    passengers_in_5_buses = 5 * avg_passengers_per_bus

    # return the result
    result = passengers_in_5_buses
    return result

print(solution())