def solution():
    """ A passenger train transports passengers between two stations located in two separate cities. On a particular day, the train carried 100 passengers from one station to the other one way, and on the return trip carried 60 passengers. If the train made three more round trips that day, taking the same number of people as the first trip in each trip, calculate the total number of passengers transported between both stations? """
    # Define the number of passengers on the first trip
    first_trip_passengers = 100

    # Calculate the number of passengers on the return trip
    return_trip_passengers = 60

    # Calculate the total number of passengers on the first round trip
    first_round_trip_passengers = first_trip_passengers + return_trip_passengers

    # Calculate the total number of passengers on all the round trips
    total_round_trip_passengers = first_round_trip_passengers * 4

    # Calculate the total number of passengers transported one way between the two stations
    total_passengers = (first_trip_passengers + return_trip_passengers + total_round_trip_passengers) * 2

    # Display the total number of passengers transported
    result = total_passengers
    return result

print(solution())