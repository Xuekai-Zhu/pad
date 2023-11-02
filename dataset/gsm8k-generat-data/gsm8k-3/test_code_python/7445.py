def solution():
    """There were 50 people on the city bus. At the first stop, 15 people got off. At the next stop 8 people got off and 2 got on. At the third stop, 4 people got off and 3 people got on. How many people are on the bus after the third stop?"""
    # Define the initial number of people on the bus
    initial_occupants = 50

    # Calculate the number of people on the bus after the first stop
    occupants_after_first_stop = initial_occupants - 15

    # Calculate the number of people on the bus after the second stop
    occupants_after_second_stop = occupants_after_first_stop - 8 + 2

    # Calculate the number of people on the bus after the third stop
    occupants_after_third_stop = occupants_after_second_stop - 4 + 3

    # Display the number of people on the bus after the third stop
    result = occupants_after_third_stop
    return result

print(solution())