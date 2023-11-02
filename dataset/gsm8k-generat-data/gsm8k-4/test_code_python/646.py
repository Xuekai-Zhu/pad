def solution():
    """A bus has a capacity of 200 people. If it carried 3/4 of its capacity on its first trip from city A to city B and 4/5 of its capacity on its return trip, calculate the total number of people the bus carried on the two trips?"""
    # Define the capacity of the bus
    capacity = 200

    # Calculate the number of people on the first trip
    trip1 = capacity * (3/4)

    # Calculate the number of people on the return trip
    trip2 = capacity * (4/5)

    # Calculate the total number of people
    total = trip1 + trip2

    # Return the result
    result = total
    return result

print(solution())