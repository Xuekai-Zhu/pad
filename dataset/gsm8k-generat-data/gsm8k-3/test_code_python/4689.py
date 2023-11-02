def solution():
    """Benjamin collects 6 dozen eggs a day. Carla collects 3 times the number of eggs that Benjamin collects.  Trisha collects 4 dozen less than Benjamin.  How many dozen eggs do the three collect total?"""
    # Define the number of dozens of eggs collected by Benjamin
    BENJAMIN_EGGS = 6

    # Calculate the number of dozens of eggs collected by Carla
    CARLA_EGGS = BENJAMIN_EGGS * 3

    # Calculate the number of dozens of eggs collected by Trisha
    TRISHA_EGGS = BENJAMIN_EGGS - 4

    # Calculate the total number of dozens of eggs collected
    total_eggs = BENJAMIN_EGGS + CARLA_EGGS + TRISHA_EGGS

    # Display the total number of dozens of eggs
    result = total_eggs
    return result

print(solution())