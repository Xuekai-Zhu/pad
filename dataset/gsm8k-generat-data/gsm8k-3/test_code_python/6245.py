def solution():
    """Shawna has 7 acorns. Sheila has 5 times as many acorns as Shawna, but 3 fewer acorns than Danny. How many acorns do they have altogether?"""
    # Define the initial number of acorns
    shawna_acorns = 7

    # Calculate the number of acorns Sheila has
    sheila_acorns = shawna_acorns * 5

    # Calculate the number of acorns Danny has
    danny_acorns = sheila_acorns + 3

    # Calculate the total number of acorns
    total_acorns = shawna_acorns + sheila_acorns + danny_acorns

    # Display the total number of acorns
    result = total_acorns
    return result

print(solution())