def solution():
    """Norma takes her clothes to the laundry. She leaves 9 T-shirts and twice as many sweaters as T-shirts in the washer. When she returns she finds 3 sweaters and triple the number of T-shirts. How many items are missing?"""
    # Define the initial number of T-shirts and sweaters
    t_shirts = 9
    sweaters = 2 * t_shirts

    # Calculate the number of T-shirts and sweaters remaining
    t_shirts_remaining = 3 * t_shirts
    sweaters_remaining = sweaters - 3

    # Calculate the number of missing items
    missing_items = t_shirts + sweaters - t_shirts_remaining - sweaters_remaining

    # return the result
    result = missing_items
    return result

print(solution())