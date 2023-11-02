def solution():
    capacity = 200  # capacity of the bus
    first_trip = (3/4) * capacity  # number of people on the first trip
    return_trip = (4/5) * capacity  # number of people on the return trip
    total_people = first_trip + return_trip  # total number of people on the two trips
    result = total_people
    return result

print(solution())