def solution():
    """Delta, Beta and Gamma decided to share 40 donuts. Delta took 8 donuts and Beta took three times as many as Gamma. How many donuts did Gamma receive?"""
    # Define the total number of donuts and the number Delta took
    total_donuts = 40
    delta_donuts = 8

    # Calculate the number of donuts left after Delta took his share
    remaining_donuts = total_donuts - delta_donuts

    # Calculate the number of donuts Beta took
    beta_donuts = 3 * gamma_donuts

    # Calculate the number of donuts Gamma received
    gamma_donuts = (remaining_donuts - beta_donuts) / 4

    result = gamma_donuts
    return result

print(solution())