def solution():
    """A bus has a capacity of 200 people. If it carried 3/4 of its capacity on its first trip from city A to city B and 4/5 of its capacity on its return trip, calculate the total number of people the bus carried on the two trips?"""
    # Define the capacity of the bus
    BUS_CAPACITY = 200

    # Calculate the number of people carried on the first trip
    first_trip = BUS_CAPACITY * 3/4

    # Calculate the number of people carried on the return trip
    return_trip = BUS_CAPACITY * 4/5

    # Calculate the total number of people carried
    total_people = first_trip + return_trip

    # Display the total number of people carried
    result = total_people
    return result

print(solution())