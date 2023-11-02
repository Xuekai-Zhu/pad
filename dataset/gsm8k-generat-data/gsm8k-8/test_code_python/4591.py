def solution():
    # Calculate the total number of sodas Tina bought
    total_sodas = 3 * 12

    # Calculate the total number of sodas consumed at the party
    total_consumed = (6 / 2) * 3 + 2 * 4 + 5

    # Calculate the number of sodas left over
    sodas_left = total_sodas - total_consumed
    result = sodas_left
    return result

print(solution())