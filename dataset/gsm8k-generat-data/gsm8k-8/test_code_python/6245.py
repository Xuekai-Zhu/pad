def solution():
    # Define the number of acorns Shawna has
    shawna_acorns = 7

    # Calculate the number of acorns Sheila has
    sheila_acorns = 5 * shawna_acorns

    # Calculate the number of acorns Danny has
    danny_acorns = sheila_acorns + 3

    # Calculate the total number of acorns
    total_acorns = shawna_acorns + sheila_acorns + danny_acorns
    result = total_acorns
    return result

print(solution())