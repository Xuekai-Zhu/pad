def solution():
    # Calculate the number of people on each bus
    bus_1 = 12
    bus_2 = 2 * bus_1
    bus_3 = bus_2 - 6
    bus_4 = bus_1 + 9

    # Calculate the total number of people going to the museum
    total_people = bus_1 + bus_2 + bus_3 + bus_4
    result = total_people
    return result

print(solution())