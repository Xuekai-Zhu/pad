def solution():
    num_cows = 12
    num_sheep = num_cows * 2
    num_pigs_per_sheep = 3

    # Calculate the number of pigs Adam will buy
    num_pigs = num_sheep * num_pigs_per_sheep

    # Calculate the total number of animals on the farm after the transaction
    total_animals = num_cows + num_sheep + num_pigs
    result = total_animals
    return result

print(solution())