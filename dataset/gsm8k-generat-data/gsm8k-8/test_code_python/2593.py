def solution():
    # Define the original number of cows and sheep
    num_cows = 12
    num_sheep = 2*num_cows

    # Calculate the number of pigs Adam bought
    num_pigs = 3*num_sheep

    # Calculate the total number of animals on the farm after the transaction
    total_animals = num_cows + num_sheep + num_pigs
    result = total_animals
    return result

print(solution())