def solution():
    # Initial number of cows and sheep
    cows = 12
    sheep = 2 * cows

    # Number of pigs to buy for each sheep
    pigs_per_sheep = 3

    # Calculate the number of pigs to buy
    pigs = pigs_per_sheep * sheep

    # Total number of animals on the farm after the transaction
    total_animals = cows + sheep + pigs
    result = total_animals
    return result

print(solution())