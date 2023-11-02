def solution():
    # Define the number of people on the first bus
    bus1 = 12

    # Calculate the number of people on the second bus
    bus2 = 2 * bus1

    # Calculate the number of people on the third bus
    bus3 = bus2 - 6

    # Calculate the number of people on the fourth bus
    bus4 = bus1 + 9

    # Calculate the total number of people
    total_people = bus1 + bus2 + bus3 + bus4
    result = total_people
    return result

print(solution())