def solution():
    total_donuts = 40

    delta_donuts = 8

    beta_donuts = 3 * gamma_donuts

    # Calculate the total donuts taken by Delta and Beta
    total_taken = delta_donuts + beta_donuts

    # Calculate the remaining donuts for Gamma
    gamma_donuts = (total_donuts - total_taken) / 2

    result = gamma_donuts
    return result

print(solution())