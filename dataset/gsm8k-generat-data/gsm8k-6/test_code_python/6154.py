def solution():
    # Calculate the number of characters with each initial
    num_A = 30  # half of the characters have the initial A
    num_C = num_A // 2  # half of those with A have C
    num_E = num_A // 4  # a quarter of those with A have E
    num_D = 2 * num_E  # twice as many with D as with E
    total_characters = num_A + num_C + num_D + num_E  # total number of characters

    # Return the number of characters with the initial D
    result = num_D
    return result

print(solution())