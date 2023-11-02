def solution():
    """There are 4 carriages in a train and each carriage has 25 seats. If each carriage could accommodate 10 more passengers, how many passengers would fill up 3 trains?"""
    # Define the number of carriages in a train and the number of seats in each carriage
    CARRIAGES = 4
    SEATS_PER_CARRIAGE = 25

    # Define the additional number of passengers each carriage could accommodate
    ADDITIONAL_PASSENGERS_PER_CARRIAGE = 10

    # Calculate the new number of seats in each carriage
    new_seats_per_carriage = SEATS_PER_CARRIAGE + ADDITIONAL_PASSENGERS_PER_CARRIAGE

    # Calculate the total number of seats in a train
    total_seats_per_train = CARRIAGES * new_seats_per_carriage

    # Calculate the number of passengers that could fill up 3 trains
    passengers = total_seats_per_train * 3

    # Display the number of passengers
    result = passengers
    return result

print(solution())