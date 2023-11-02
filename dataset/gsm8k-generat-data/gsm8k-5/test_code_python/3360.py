def solution():
    original_animals = 5
    additional_animals = 4
    total_animals = original_animals + additional_animals
    time_per_type = 6  # Time in minutes to see each animal type

    # Calculate the total time to see all animal types
    total_time = total_animals * time_per_type
    result = total_time
    return result

print(solution())