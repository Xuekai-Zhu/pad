def solution():
    """A supermarket has 2355 loaves of bread at the start of the day. By afternoon, 629 loaves are sold, and a further 489 loaves are delivered to the supermarket by their supplier in the evening. How many loaves of bread are there at the end of the day?"""
    # Define the initial number of loaves
    INITIAL_LOAVES = 2355

    # Define the number of loaves sold and delivered
    LOAVES_SOLD = 629
    LOAVES_DELIVERED = 489

    # Calculate the number of loaves remaining at the end of the day
    loaves_remaining = INITIAL_LOAVES - LOAVES_SOLD + LOAVES_DELIVERED

    # Display the number of loaves remaining
    result = loaves_remaining
    return result

print(solution())