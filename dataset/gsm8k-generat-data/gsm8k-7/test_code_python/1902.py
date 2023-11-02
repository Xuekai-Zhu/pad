def solution():
    num_antelopes = 80
    num_rabbits = num_antelopes + 34
    num_hyenas = (num_antelopes + num_rabbits) - 42
    num_wild_dogs = num_hyenas + 50
    num_leopards = num_rabbits / 2

    # Calculate the total number of animals
    total_animals = num_antelopes + num_rabbits + num_hyenas + num_wild_dogs + num_leopards
    result = total_animals
    return result

print(solution())