def solution():
    total_donuts = 40  # The total number of donuts is 40
    delta_donuts = 8  # Delta took 8 donuts
    beta_donuts = 3 * gamma_donuts  # Beta took three times as many donuts as Gamma took

    # Calculate the number of donuts Gamma received
    gamma_donuts = (total_donuts - delta_donuts - beta_donuts) / 5
    result = gamma_donuts
    return result

print(solution())