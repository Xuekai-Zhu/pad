def solution():
    """A supermarket has 2355 loaves of bread at the start of the day. By afternoon, 629 loaves are sold, and a further 489 loaves are delivered to the supermarket by their supplier in the evening. How many loaves of bread are there at the end of the day?"""
    starting_loaves = 2355
    sold_loaves = 629
    delivered_loaves = 489
    ending_loaves = starting_loaves - sold_loaves + delivered_loaves
    result = ending_loaves
    return result

print(solution())