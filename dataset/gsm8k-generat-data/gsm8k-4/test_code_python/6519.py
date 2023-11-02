def solution():
    """A snail kite is a kind of bird that eats apple snails. On the first day, a snail kite ate 3 snails. Then it eats 2 more snails than it did the day before. How many apple snails in all did a snail kite eat for 5 days?"""
    # Initialize the total snails eaten to 0
    total_snails_eaten = 0

    # Start with the first day
    snails_eaten = 3

    # Add the snails eaten on each day for a total of 5 days
    for day in range(1, 6):
        total_snails_eaten += snails_eaten
        snails_eaten += 2

    # return the result
    result = total_snails_eaten
    return result

print(solution())