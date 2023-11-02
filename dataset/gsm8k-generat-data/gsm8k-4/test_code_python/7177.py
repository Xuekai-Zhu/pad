def solution():
    """5 geckos on the kitchen window eat 6 insects each. 3 lizards eat twice as much as the geckos. How many total insects were eaten?"""
    # Define the number of geckos and the number of insects they eat
    geckos = 5
    gecko_insects = 6

    # Calculate the total number of insects eaten by the geckos
    gecko_total_insects = geckos * gecko_insects

    # Define the number of lizards and the number of insects they eat relative to the geckos
    lizards = 3
    lizard_to_gecko_ratio = 2

    # Calculate the number of insects each lizard eats
    lizard_insects = gecko_insects * lizard_to_gecko_ratio

    # Calculate the total number of insects eaten by the lizards
    lizard_total_insects = lizards * lizard_insects

    # Calculate the total number of insects eaten by all the reptiles
    total_insects = gecko_total_insects + lizard_total_insects

    result = total_insects
    return result

print(solution())