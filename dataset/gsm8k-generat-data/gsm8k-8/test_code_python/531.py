def solution():
    # Define the number of animals that escaped
    lions = 3
    rhinos = 2

    # Define the time it takes to recover each animal
    time_per_animal = 2

    # Calculate the total time spent recovering animals
    total_time = (lions + rhinos) * time_per_animal
    result = total_time
    return result

print(solution())