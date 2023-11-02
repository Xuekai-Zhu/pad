def solution():
    """When it rains, the three holes in the garage roof leak water at different rates.
    The largest hole leaks at a rate of 3 ounces of water per minute.
    The medium-sized hole leaks water at one-half the rate of the largest hole.
    And the smallest hole leaks water at a rate of one-third the rate of the medium-sized hole.
    When it rains, what is the combined amount of water, in ounces, that leak from all three holes over a 2-hour time period?"""
    # Define the leak rates of the three holes
    largest_rate = 3
    medium_rate = largest_rate / 2
    smallest_rate = medium_rate / 3

    # Calculate the amount of water leaked from each hole in 2 hours
    largest_leak = largest_rate * 60 * 2
    medium_leak = medium_rate * 60 * 2
    smallest_leak = smallest_rate * 60 * 2

    # Calculate the total amount of water leaked from all three holes
    total_leak = largest_leak + medium_leak + smallest_leak

    result = total_leak
    return result

print(solution())