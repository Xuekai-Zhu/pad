def solution():
    capacity = 200

    # Calculate the number of people on the first trip
    first_trip = int(capacity * (3/4))

    # Calculate the number of people on the return trip
    return_trip = int(capacity * (4/5))

    # Calculate the total number of people the bus carried
    total_people = first_trip + return_trip
    result = total_people
    return result

print(solution())