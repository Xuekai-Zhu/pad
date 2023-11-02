def solution():
    num_lions = 200

    # Calculate the number of leopards
    num_leopards = num_lions / 2

    # Calculate the combined number of lions and leopards
    total_lions_leopards = num_lions + num_leopards

    # Calculate the number of elephants
    num_elephants = total_lions_leopards / 2

    # Calculate the total population of all animals
    total_population = num_lions + num_leopards + num_elephants
    result = total_population
    return result

print(solution())