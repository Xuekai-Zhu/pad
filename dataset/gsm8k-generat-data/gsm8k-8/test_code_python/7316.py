def solution():
    # Calculate the total number of pickles he can make
    total_pickles = min(4 * 12, 10 * 6)

    # Calculate the total amount of vinegar he needs
    total_vinegar = total_pickles * 10

    # Calculate the amount of vinegar left
    vinegar_left = 100 - total_vinegar
    result = vinegar_left
    return result

print(solution())