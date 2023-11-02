def solution():
    """Zara bought 24 cows, 7 sheep, and some goats. Next week, she will transport all of them to a new farm in 3 equally-sized groups of 48 animals per group. How many goats does she own?"""
    # Define the number of cows and sheep
    cows = 24
    sheep = 7

    # Calculate the total number of animals
    total_animals = cows + sheep + x

    # Calculate the number of goats
    goats = total_animals - 3 * 48

    result = goats
    return result

# We can solve for the number of goats by rearranging the equation:
# total_animals = 3 * 48 = 144
# goats = total_animals - cows - sheep = 144 - 24 - 7 = 113.
# Therefore, Zara owns 113 goats.

print(solution())