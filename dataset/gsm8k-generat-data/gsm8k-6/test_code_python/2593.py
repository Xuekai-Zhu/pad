def solution():
    # Calculate the number of sheep and pigs Adam had
    num_sheep = 12 * 2  # twice as many sheep as cows
    num_pigs = 3 * num_sheep  # 3 pigs for every sheep

    # Calculate the total number of animals on the farm after the transaction
    total_animals = 12 + num_sheep + num_pigs
    result = total_animals
    return result

print(solution())