def solution():
    """Zara bought 24 cows, 7 sheep, and some goats. Next week, she will transport all of them to a new farm in 3 equally-sized groups of 48 animals per group. How many goats does she own?"""
    # Define the number of cows and sheep
    cows = 24
    sheep = 7

    # Define the total number of animals
    total_animals = cows + sheep + x  # let x be the number of goats

    # Define the number of groups
    num_groups = 3

    # Define the size of each group
    group_size = 48

    # Calculate the number of goats
    goat_count = (num_groups * group_size) - (cows + sheep)

    # Display the number of goats
    result = goat_count
    return result

print(solution())