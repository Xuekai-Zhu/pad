def solution():
    """Benjamin collects 6 dozen eggs a day. Carla collects 3 times the number of eggs that Benjamin collects. Trisha collects 4 dozen less than Benjamin. How many dozen eggs do the three collect total?"""
    # Define the number of eggs collected by Benjamin
    benjamin_eggs = 6 * 12

    # Define the number of eggs collected by Carla
    carla_eggs = 3 * benjamin_eggs

    # Define the number of eggs collected by Trisha
    trisha_eggs = (6 - 4) * 12

    # Calculate the total number of eggs collected
    total_eggs = benjamin_eggs + carla_eggs + trisha_eggs

    # Convert the total number of eggs to dozens
    total_dozen = total_eggs / 12

    result = total_dozen
    return result

print(solution())