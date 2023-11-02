def solution():
    """Norma takes her clothes to the laundry. She leaves 9 T-shirts and twice as many sweaters as T-shirts in the washer. When she returns she finds 3 sweaters and triple the number of T-shirts. How many items are missing?"""
    # Define the initial number of T-shirts and sweaters
    t_shirts = 9
    sweaters = 2 * t_shirts

    # Define the number of T-shirts and sweaters when Norma returns
    t_shirts_returned = 3 * t_shirts
    sweaters_returned = 3 * sweaters

    # Calculate the total number of items when Norma returns
    total_items_returned = t_shirts_returned + sweaters_returned

    # Calculate the number of missing items
    missing_items = (t_shirts + sweaters) - total_items_returned

    # Display the number of missing items
    result = missing_items
    return result

print(solution())