def solution():
    """Brinley's teacher took the grade six students to the San Diego Zoo to watch and learn about animals. While at the zoo, Brinley counted 100 snakes, 80 arctic foxes, and 20 leopards. She also saw ten times more bee-eaters than leopards, half as many cheetahs as snakes, and twice as many alligators as the total number of Arctic foxes and leopards. What's the total number of animals Brinley counted at the zoo?"""
    # Define the number of snakes, arctic foxes and leopards observed by Brinley
    snakes = 100
    arctic_foxes = 80
    leopards = 20

    # Calculate the number of bee-eaters
    bee_eaters = 10 * leopards

    # Calculate the number of cheetahs
    cheetahs = snakes / 2

    # Calculate the total number of arctic foxes and leopards
    total_foxes_leopards = arctic_foxes + leopards

    # Calculate the number of alligators
    alligators = 2 * total_foxes_leopards

    # Calculate the total number of animals observed by Brinley
    total_animals = snakes + arctic_foxes + leopards + bee_eaters + cheetahs + alligators

    # return the result
    result = total_animals
    return result

print(solution())