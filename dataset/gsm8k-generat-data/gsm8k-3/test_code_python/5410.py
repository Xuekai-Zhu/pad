def solution():
    """James is trying to decide which trail is faster to hike. One trail is 20 miles and mostly downhill, so James can cover it at 5 miles per hour. The other trail is 12 miles, but it's mostly uphill, so James will only be able to cover 3 miles per hour and will have to take an hour break halfway through. How many hours faster is the fastest hike?"""
    # Calculate the time it takes to hike the first trail
    time1 = 20 / 5

    # Calculate the time it takes to hike the second trail
    time2 = 6 + (12 / 3) + 1

    # Compare the times and calculate the difference
    if time1 < time2:
        difference = time2 - time1
    else:
        difference = time1 - time2

    # Display the difference in time
    result = difference
    return result

print(solution())