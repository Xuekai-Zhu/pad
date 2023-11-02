def solution():
    """At a station, a train comes every 5 minutes leaving 200 passengers and taking 320 others. How many different passengers step on and off a train at the station within an hour?"""
    passengers_in = 200
    passengers_out = 320
    # calculate the total number of passengers that step on and off the train in one hour
    # 60 minutes in an hour, and 5 minutes per train, so there are 12 trains per hour
    total_passengers = 12 * (passengers_in + passengers_out)
    result = total_passengers
    return result

print(solution())