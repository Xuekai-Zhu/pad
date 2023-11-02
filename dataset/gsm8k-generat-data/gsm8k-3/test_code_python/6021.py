def solution():
    """Harry is traveling home on the bus. He has already been sat on the bus for 15 minutes, and he knows the rest of the journey will take another 25 minutes. The walk from the bus stop to his house will take half the amount of time the bus journey took. In total, how many minutes will Harry have spent traveling?"""
    # Define the amount of time Harry spends on the bus
    bus_time = 15 + 25

    # Define the amount of time Harry spends walking
    walk_time = bus_time / 2

    # Calculate the total travel time
    total_time = bus_time + walk_time

    # Display the total travel time in minutes
    result = total_time
    return result

print(solution())