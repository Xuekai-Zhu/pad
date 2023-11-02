def solution():
    """A passenger train transports passengers between two stations located in two separate cities.
    On a particular day, the train carried 100 passengers from one station to the other one way,
    and on the return trip carried 60 passengers.
    If the train made three more round trips that day, taking the same number of people as the first trip in each trip,
    calculate the total number of passengers transported between both stations?"""
    one_way_passengers = 100
    return_passengers = 60
    round_trip_passengers = one_way_passengers + return_passengers
    total_passengers = (round_trip_passengers * 2) + (round_trip_passengers * 3)
    result = total_passengers
    return result

print(solution())