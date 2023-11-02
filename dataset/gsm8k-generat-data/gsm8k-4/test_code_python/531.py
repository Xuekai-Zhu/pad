def solution():
    """3 lions and 2 rhinos escape from the zoo. If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?"""
    # Define the number of lions and rhinos that escaped
    lions = 3
    rhinos = 2

    # Define the time it takes to recover each animal
    recovery_time = 2

    # Calcualte the total time spent recovering all the animals
    total_recovery_time = (lions + rhinos) * recovery_time

    # return the result
    result = total_recovery_time
    return result

print(solution())