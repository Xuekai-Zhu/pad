def solution():
    num_cows = 4
    num_sheep = 3
    num_chickens = 7
    cow_sheep_food = 2
    chicken_food = 3

    # Calculate the total food needed for cows and sheep
    total_cow_sheep_food = (num_cows + num_sheep) * cow_sheep_food

    # Calculate the total food needed for chickens
    total_chicken_food = num_chickens * chicken_food

    # Calculate the total food needed for all animals
    total_food = total_cow_sheep_food + total_chicken_food
    result = total_food
    return result

print(solution())