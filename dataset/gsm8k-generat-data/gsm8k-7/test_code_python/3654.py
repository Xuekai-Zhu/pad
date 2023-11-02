def solution():
    num_cows = 20
    num_ducks = num_cows * 1.5
    num_pigs = (num_cows + num_ducks) / 5
    total_animals = num_cows + num_ducks + num_pigs
    result = total_animals
    return result

print(solution())