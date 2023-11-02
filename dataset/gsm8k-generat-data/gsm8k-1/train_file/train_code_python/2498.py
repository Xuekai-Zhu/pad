def solution():
    """A supermarket has 2355 loaves of bread at the start of the day. By afternoon, 629 loaves are sold, and a further 489 loaves are delivered to the supermarket by their supplier in the evening. How many loaves of bread are there at the end of the day?"""
    starting_loaves = 2355
    loaves_sold = 629
    loaves_delivered = 489
    total_loaves = starting_loaves - loaves_sold + loaves_delivered
    result = total_loaves
    return result

print(solution())