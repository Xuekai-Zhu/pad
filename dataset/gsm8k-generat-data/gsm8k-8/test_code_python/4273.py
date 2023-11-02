def solution():
    # Define the number of each animal Brinley counted
    snakes = 100
    arctic_foxes = 80
    leopards = 20
    bee_eaters = 10 * leopards
    cheetahs = 0.5 * snakes
    alligators = 2 * (arctic_foxes + leopards)

    # Calculate the total number of animals Brinley counted
    total_animals = snakes + arctic_foxes + leopards + bee_eaters + cheetahs + alligators
    result = total_animals
    return result

print(solution())