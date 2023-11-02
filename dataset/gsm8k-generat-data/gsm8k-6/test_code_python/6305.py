def solution():
    # Find the number of donuts Beta took
    beta_donuts = 40 - 8  # the remaining donuts after Delta took 8
    gamma_donuts = beta_donuts / 4  # Beta took three times as many as Gamma
    result = gamma_donuts
    return result

print(solution())