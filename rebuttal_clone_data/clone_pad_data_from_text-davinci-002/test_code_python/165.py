def solution():
    """Manex is a tour bus driver. He has to drive 55 miles to the destination and drive going back to the starting point on a different way that is 10 miles farther. If he can drive 1 mile for 2 minutes and stayed 2 hours at the destination, how long will it take the bus driver to do the entire tour in hours?"""
    miles_to_destination = 55
    miles_back = 65
    minutes_per_mile = 2
    minutes_at_destination = 120
    total_minutes = minutes_per_mile * (miles_to_destination + miles_back) + minutes_at_destination
    hours = total_minutes / 60
    result = hours
    return result

print(solution())