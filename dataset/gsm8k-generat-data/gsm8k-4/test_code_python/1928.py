def solution():
    """A passenger train transports passengers between two stations located in two separate cities. On a particular day, the train carried 100 passengers from one station to the other one way, and on the return trip carried 60 passengers. If the train made three more round trips that day, taking the same number of people as the first trip in each trip, calculate the total number of passengers transported between both stations?"""
    # Define the total number of passengers transported on the first trip
    first_trip_passengers = 100

    # Define the total number of passengers transported on the return trip
    return_trip_passengers = 60

    # Define the number of additional round trips made by the train
    additional_round_trips = 3

    # Calculate the total number of passengers transported on the additional round trips
    additional_passengers = first_trip_passengers * 2 * additional_round_trips

    # Calculate the total number of passengers transported on both trips
    total_passengers = (first_trip_passengers + return_trip_passengers) * 2 + additional_passengers

    # return the result
    result = total_passengers
    return result

print(solution())