def solution():
    """At a station, a train comes every 5 minutes leaving 200 passengers and taking 320 others.
     How many different passengers step on and off a train at the station within an hour?"""
    
    # Define the number of passengers leaving and taking the train every 5 minutes
    passengers_leaving = 200
    passengers_taking = 320

    # Calculate the total number of passengers per train
    total_passengers = passengers_leaving + passengers_taking

    # Calculate the number of trains per hour
    trains_per_hour = 60 // 5     #60 minutes per hour, with a train every 5 minutes

    # Calculate the total number of passengers in an hour
    total_passengers_per_hour = total_passengers * trains_per_hour

    # Calculate the number of different passengers
    different_passengers = total_passengers_per_hour // 2   #Each passenger counts twice, as they step on and off

    # Display the number of different passengers
    result = different_passengers
    return result

print(solution())