def solution():
    # Define the capacity of the bus
    capacity = 200

    # Calculate the number of people on the first trip
    first_trip = int(capacity * 3/4)

    # Calculate the number of people on the return trip
    return_trip = int(capacity * 4/5)

    # Calculate the total number of people carried
    total = first_trip + return_trip
    result = total
    return result

print(solution())