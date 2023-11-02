def solution():
    # Calculate the time to recover each individual animal
    time_per_animal = 2  # It takes 2 hours to recover each animal

    # Calculate the total time spent recovering all the escaped animals
    total_time = time_per_animal * 5  # There are 3 lions and 2 rhinos

    result = total_time
    return result

print(solution())