def solution():
    """Darma can eat 20 peanuts in 15 seconds. At this same rate, how many peanuts could she eat in 6 minutes?"""
    # Define the rate of eating peanuts in peanuts per second
    rate = 20 / 15

    # Convert the duration of 6 minutes to seconds
    duration = 6 * 60

    # Calculate the total number of peanuts that can be eaten in the given duration
    peanuts = rate * duration

    # Return the result
    result = peanuts
    return result

print(solution())