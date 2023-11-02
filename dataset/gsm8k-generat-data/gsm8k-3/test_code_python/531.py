def solution():
    """3 lions and 2 rhinos escape from the zoo.  If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?"""
    # Define the number of lions and rhinos that escaped
    lions_escaped = 3
    rhinos_escaped = 2

    # Define the time it takes to recover an animal in hours
    time_per_animal = 2

    # Calculate the total time spent recovering animals
    total_time = (lions_escaped + rhinos_escaped) * time_per_animal

    # Display the total time spent recovering animals
    result = total_time
    return result

print(solution())