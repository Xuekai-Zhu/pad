def solution():
    """The school is organizing a trip to the museum. 4 buses were hired to take the children and teachers to their destination. The second bus has twice the number of people on it as the first bus. The third bus has 6 fewer people than the second bus. The fourth bus has 9 more people than the first bus. If the first bus has 12 people, how many people are going to the museum in total?"""
    # Define the number of people on the first bus
    bus1 = 12

    # Calculate the number of people on the second bus
    bus2 = bus1 * 2

    # Calculate the number of people on the third bus
    bus3 = bus2 - 6

    # Calculate the number of people on the fourth bus
    bus4 = bus1 + 9

    # Calculate the total number of people going to the museum
    total_people = bus1 + bus2 + bus3 + bus4

    # return the result
    result = total_people
    return result

print(solution())