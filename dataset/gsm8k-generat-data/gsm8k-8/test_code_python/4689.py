def solution():
    # Calculate the number of eggs collected by Benjamin
    benjamin_eggs = 6 * 12

    # Calculate the number of eggs collected by Carla
    carla_eggs = 3 * benjamin_eggs

    # Calculate the number of eggs collected by Trisha
    trisha_eggs = (6 - 4) * 12  # Trisha collects 4 dozen less than Benjamin

    # Calculate the total number of eggs collected
    total_eggs = benjamin_eggs + carla_eggs + trisha_eggs

    # Convert the total number of eggs to dozens
    total_dozen = total_eggs / 12

    result = total_dozen
    return result

print(solution())