def solution():
    num_animal_types = 5
    time_per_type = 6
    num_new_species = 4

    # Calculate the total number of animal types
    total_animal_types = num_animal_types + num_new_species

    # Calculate the total time it would take to see each animal type
    total_time = total_animal_types * time_per_type
    result = total_time
    return result

print(solution())