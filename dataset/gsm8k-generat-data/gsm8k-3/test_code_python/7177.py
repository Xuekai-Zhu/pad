def solution():
    """5 geckos on the kitchen window eat 6 insects each. 3 lizards eat twice as much as the geckos.  How many total insects were eaten?"""
    # Calculate the total number of insects eaten by the geckos
    gecko_insects = 5 * 6

    # Calculate the number of insects eaten by each lizard
    lizard_insects = 2 * gecko_insects

    # Calculate the total number of insects eaten by the lizards
    total_lizard_insects = 3 * lizard_insects

    # Calculate the total number of insects eaten by all the animals
    total_insects = gecko_insects + total_lizard_insects

    # Display the total number of insects eaten
    result = total_insects
    return result

print(solution())