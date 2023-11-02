def solution():
    """Delta, Beta and Gamma decided to share 40 donuts. Delta took 8 donuts and Beta took three times as many as Gamma. How many donuts did Gamma receive?"""
    total_donuts = 40
    delta_donuts = 8
    beta_donuts = 3 * gamma_donuts
    gamma_donuts = (total_donuts - delta_donuts - beta_donuts)
    result = gamma_donuts
    return result

print(solution())