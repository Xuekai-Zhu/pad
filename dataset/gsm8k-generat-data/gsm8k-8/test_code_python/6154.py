def solution():
    # Calculate the number of characters with the initial A
    num_A = 60 // 2

    # Calculate the number of characters with the initial C
    num_C = num_A // 2

    # Calculate the total number of characters with the initial D and E
    num_D_E = 60 - num_A - num_C

    # Calculate the number of characters with the initial E
    num_E = num_D_E // 3

    # Calculate the number of characters with the initial D
    num_D = num_E * 2

    result = num_D
    return result

print(solution())