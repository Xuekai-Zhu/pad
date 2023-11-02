def solution():
    """3 lions and 2 rhinos escape from the zoo. If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?"""
    num_lions = 3
    num_rhinos = 2
    time_per_animal = 2
    total_recovery_time = (num_lions + num_rhinos) * time_per_animal
    result = total_recovery_time
    return result

print(solution())