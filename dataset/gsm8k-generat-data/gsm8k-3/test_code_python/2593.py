def solution():
    """Adam had a farm with animals. He had 12 cows and twice as many sheep. He decided to buy 3 pigs for every sheep he had. How many animals were on the farm after the transaction?"""
    # Define the number of cows and sheep on the farm
    cows = 12
    sheep = cows * 2

    # Calculate the number of pigs Adam buys for each sheep
    pigs_per_sheep = 3

    # Calculate the total number of pigs Adam needs to buy
    pigs = sheep * pigs_per_sheep

    # Calculate the total number of animals on the farm after the transaction
    total_animals = cows + sheep + pigs

    # Display the total number of animals
    result = total_animals
    return result

print(solution())