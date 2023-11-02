def solution():
    snakes = 100
    arctic_foxes = 80
    leopards = 20

    # Calculate the number of bee-eaters
    bee_eaters = 10 * leopards

    # Calculate the number of cheetahs
    cheetahs = snakes / 2

    # Calculate the total number of alligators
    alligators = 2 * (arctic_foxes + leopards)

    # Calculate the total number of animals Brinley counted
    total_animals = snakes + arctic_foxes + leopards + bee_eaters + cheetahs + alligators
    result = total_animals
    return result

print(solution())