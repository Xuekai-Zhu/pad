def solution():
    """There are 4 carriages in a train and each carriage has 25 seats. If each carriage could accommodate 10 more passengers, how many passengers would fill up 3 trains?"""
    # Define the number of carriages per train, the number of seats per carriage, and the additional passengers per carriage
    carriages_per_train = 4
    seats_per_carriage = 25
    additional_passengers = 10

    # Calculate the new capacity per carriage
    new_capacity = seats_per_carriage + additional_passengers

    # Calculate the total capacity per train
    total_capacity_per_train = new_capacity * carriages_per_train

    # Calculate the total number of passengers for 3 trains
    passengers = total_capacity_per_train * 3

    # Return the result
    result = passengers
    return result

print(solution())