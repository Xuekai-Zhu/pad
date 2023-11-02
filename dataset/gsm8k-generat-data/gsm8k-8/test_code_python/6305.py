def solution():
    # Define the number of donuts Delta took
    delta_donuts = 8

    # Calculate the total donuts taken by Delta and Beta
    delta_beta_donuts = 40 - delta_donuts

    # Calculate the donuts taken by Gamma
    gamma_donuts = delta_beta_donuts / 4

    result = gamma_donuts
    return result

print(solution())