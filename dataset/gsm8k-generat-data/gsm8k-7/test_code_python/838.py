def solution():
    num_sheep = 20
    num_cows = 10
    num_dogs = 14

    # Calculate the number of sheep that did not make it to shore
    num_sheep_drowned = 3

    # Calculate the number of cows that did not make it to shore
    num_cows_drowned = num_sheep_drowned * 2

    # Calculate the total number of animals that did not make it to shore
    num_animals_lost = num_sheep_drowned + num_cows_drowned

    # Calculate the total number of animals that made it to shore
    num_animals_survived = num_sheep + num_cows + num_dogs - num_animals_lost

    result = num_animals_survived
    return result

print(solution())