def solution():
    num_lions = 3
    num_rhinos = 2
    time_per_animal = 2

    # Calculate the total number of animals that need to be recovered
    total_animals = num_lions + num_rhinos

    # Calculate the total time needed to recover all animals
    total_time = total_animals * time_per_animal
    result = total_time
    return result

print(solution())