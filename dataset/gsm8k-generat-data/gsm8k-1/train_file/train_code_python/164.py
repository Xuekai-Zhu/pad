def solution():
    """Manex is a tour bus driver. He has to drive 55 miles to the destination and drive going back to the starting point on a different way that is 10 miles farther. If he can drive 1 mile for 2 minutes and stayed 2 hours at the destination, how long will it take the bus driver to do the entire tour in hours?"""
    miles_to_destination = 55
    miles_on_return_trip = 55 + 10
    minutes_per_mile = 2
    time_to_drive = (miles_to_destination + miles_on_return_trip) * minutes_per_mile
    time_at_destination = 2 * 60
    total_time = (time_to_drive + time_at_destination) / 60 / 60
    result = total_time
    return result

print(solution())