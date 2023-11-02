def solution():
    """A supermarket has 2355 loaves of bread at the start of the day. By afternoon, 629 loaves are sold, and a further 489 loaves are delivered to the supermarket by their supplier in the evening. How many loaves of bread are there at the end of the day?"""
    # Define the initial number of loaves of bread
    initial_loaves = 2355

    # Subtract the number of loaves sold
    remaining_loaves = initial_loaves - 629

    # Add the number of loaves delivered
    final_loaves = remaining_loaves + 489

    # return the result
    result = final_loaves
    return result

print(solution())