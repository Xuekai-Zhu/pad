def solution():
    """Delta, Beta and Gamma decided to share 40 donuts. Delta took 8 donuts and Beta took three times as many as Gamma. How many donuts did Gamma receive?"""
    # Define the total number of donuts
    total_donuts = 40

    # Define the number of donuts taken by Delta
    delta_donuts = 8

    # Calculate the remaining number of donuts
    remaining_donuts = total_donuts - delta_donuts

    # Calculate the number of donuts taken by Beta
    beta_donuts = remaining_donuts // 4 * 3

    # Calculate the number of donuts taken by Gamma
    gamma_donuts = remaining_donuts - beta_donuts

    # Display the number of donuts Gamma received
    result = gamma_donuts
    return result

print(solution())