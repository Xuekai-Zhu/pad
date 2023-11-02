def solution():
    num_snakes = 100
    num_arctic_foxes = 80
    num_leopards = 20

    # Calculate the number of bee-eaters
    num_bee_eaters = 10 * num_leopards

    # Calculate the number of cheetahs
    num_cheetahs = num_snakes / 2

    # Calculate the total number of alligators
    num_alligators = 2 * (num_arctic_foxes + num_leopards)

    # Calculate the total number of animals Brinley saw
    total_animals = num_snakes + num_arctic_foxes + num_leopards + num_bee_eaters + num_cheetahs + num_alligators
    result = total_animals
    return result

print(solution())