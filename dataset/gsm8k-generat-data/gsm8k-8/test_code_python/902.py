def solution():
    # Calculate the number of straws fed to the adult pigs
    adult_pigs_straws = 300 * 3/5

    # Calculate the total number of straws given to the piglets
    total_piglets_straws = adult_pigs_straws / 2

    # Calculate the number of straws each piglet ate
    each_piglet_straws = total_piglets_straws / 20
    result = each_piglet_straws
    return result

print(solution())