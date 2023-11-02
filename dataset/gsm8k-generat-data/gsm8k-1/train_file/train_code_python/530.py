def solution():
    """3 lions and 2 rhinos escape from the zoo. If it takes 2 hours to recover each animal how long did the zoo spend recovering animals?"""
    lions = 3
    rhinos = 2
    animals = lions + rhinos
    recovery_time = 2
    total_recovery_time = animals * recovery_time
    result = total_recovery_time
    return result

print(solution())