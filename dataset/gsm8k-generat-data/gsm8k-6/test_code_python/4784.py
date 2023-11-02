def solution():
    # Calculate the total number of leopards in the park
    num_lions = 200
    num_leopards = num_lions / 2

    # Calculate the total number of elephants in the park
    num_elephants = (num_lions + num_leopards) / 2

    # Calculate the total population of the three animals
    total_population = num_lions + num_leopards + num_elephants
    result = total_population
    return result

print(solution())