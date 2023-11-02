def solution():
    """A bus has a capacity of 200 people. If it carried 3/4 of its capacity on its first trip from city A to city B and 4/5 of its capacity on its return trip, calculate the total number of people the bus carried on the two trips?"""
    capacity = 200
    first_trip = capacity * (3/4)
    return_trip = capacity * (4/5)
    total_people = first_trip + return_trip
    result = total_people
    return result

print(solution())