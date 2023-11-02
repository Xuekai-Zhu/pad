def solution():
    capacity = 200  # Capacity of the bus is 200 people
    first_trip = capacity * (3/4)  # Number of people on the first trip is 3/4 of the capacity
    return_trip = capacity * (4/5)  # Number of people on the return trip is 4/5 of the capacity

    # Calculate the total number of people on the two trips
    total_people = first_trip + return_trip
    result = total_people
    return result

print(solution())