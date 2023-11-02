def solution():
    snakes = 100
    arctic_foxes = 80
    leopards = 20
    bee_eaters = snakes * 10
    cheetahs = snakes / 2
    alligators = (arctic_foxes + leopards) * 2
    total_animals = snakes + arctic_foxes + leopards + bee_eaters + cheetahs + alligators
    result = total_animals
    return result

print(solution())