def solution():
    """At a station, a train comes every 5 minutes leaving 200 passengers and taking 320 others. How many different passengers step on and off a train at the station within an hour?"""
    # Define the number of passengers leaving and boarding the train every 5 minutes
    passengers_leaving = 200
    passengers_boarding = 320

    # Calculate the number of trains arriving in an hour
    trains_per_hour = 60 / 5

    # Calculate the total number of passengers stepping on and off the train in an hour
    total_passengers = (passengers_leaving + passengers_boarding) * trains_per_hour

    result = total_passengers
    return result

print(solution())