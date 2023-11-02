def solution():
    """Darma can eat 20 peanuts in 15 seconds. At this same rate, how many peanuts could she eat in 6 minutes?"""
    # Define the number of seconds in 6 minutes
    SECONDS_IN_6_MINUTES = 360

    # Calculate the number of peanuts Darma can eat in 1 second
    peanuts_per_second = 20 / 15

    # Calculate the total number of peanuts Darma can eat in 6 minutes
    peanuts_in_6_minutes = peanuts_per_second * SECONDS_IN_6_MINUTES

    # Display the total number of peanuts Darma can eat in 6 minutes
    result = peanuts_in_6_minutes
    return result

print(solution())