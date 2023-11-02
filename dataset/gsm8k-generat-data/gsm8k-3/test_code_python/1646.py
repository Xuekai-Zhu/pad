def solution():
    """198 passengers fit into 9 buses. How many passengers fit in 5 buses?"""
    # Calculate the average number of passengers per bus
    avg_passengers = 198 / 9

    # Calculate the number of passengers that will fit in 5 buses
    passengers_in_5_buses = avg_passengers * 5

    # Display the result
    result = passengers_in_5_buses
    return result

print(solution())