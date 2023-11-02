def solution():
    """Harry is traveling home on the bus. He has already been sat on the bus for 15 minutes, and he knows the rest of the journey will take another 25 minutes. The walk from the bus stop to his house will take half the amount of time the bus journey took. In total, how many minutes will Harry have spent traveling?"""
    bus_journey_time = 25
    walk_time = bus_journey_time / 2
    total_travel_time = 15 + bus_journey_time + walk_time
    result = total_travel_time
    return result

print(solution())