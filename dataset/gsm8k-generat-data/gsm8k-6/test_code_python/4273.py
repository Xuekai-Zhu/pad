def solution():
    # Calculate the number of bee-eaters Brinley saw
    bee_eaters = 10 * 20  # ten times more bee-eaters than leopards

    # Calculate the number of cheetahs Brinley saw
    cheetahs = 1/2 * 100  # half as many cheetahs as snakes

    # Calculate the total number of alligators Brinley saw
    alligators = 2 * (80 + 20)  # twice as many alligators as the total number of Arctic foxes and leopards

    # Calculate the total number of animals Brinley saw
    total_animals = 100 + 80 + 20 + bee_eaters + cheetahs + alligators

    result = total_animals
    return result

print(solution())