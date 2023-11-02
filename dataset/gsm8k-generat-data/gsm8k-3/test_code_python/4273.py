def solution():
    """Brinley's teacher took the grade six students to the San Diego Zoo to watch and learn about animals. While at the zoo, Brinley counted 100 snakes, 80 arctic foxes, and 20 leopards. She also saw ten times more bee-eaters than leopards, half as many cheetahs as snakes, and twice as many alligators as the total number of Arctic foxes and leopards. What's the total number of animals Brinley counted at the zoo?"""
    # Define the number of each type of animal Brinley saw
    snakes = 100
    arctic_foxes = 80
    leopards = 20
    bee_eaters = 10 * leopards
    cheetahs = snakes / 2
    alligators = 2 * (arctic_foxes + leopards)

    # Calculate the total number of animals Brinley saw
    total_animals = snakes + arctic_foxes + leopards + bee_eaters + cheetahs + alligators

    # Display the total number of animals
    result = total_animals
    return result

print(solution())