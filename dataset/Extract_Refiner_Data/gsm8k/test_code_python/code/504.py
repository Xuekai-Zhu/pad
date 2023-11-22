def solution():
    
    # Define the number of cows and sheep
    farm_cows = 30
    farm_sheep = 20

    # Calculate the number of cows and sheep
    zoo_cows = farm_cows * 2
    zoo_sheep = zoo_cows * 2

    # Calculate the total number of cows and sheep
    total_cows = farm_cows + zoo_cows
    total_sheep = farm_sheep / 2

    # Calculate the total number of animals
    total_animals = total_cows + total_sheep

    # Display the total number of animals
    result = total_animals
    return result

print(solution())