def solution():
    """Emma bought 3 dozens of macarons in addition to her 10 pieces of macarons for a party. If 15 pieces of macarons are left over, how many pieces of macarons were eaten?"""
    # Define the number of macarons in a dozen
    MACARON_PER_DOZEN = 12

    # Define the number of macarons Emma bought and the number she had initially
    bought_macarons = 3 * MACARON_PER_DOZEN + 10
    initial_macarons = bought_macarons + 15 # since 15 pieces were left over

    # Calculate the number of macarons eaten
    eaten_macarons = initial_macarons - bought_macarons

    # Display the number of macarons eaten
    result = eaten_macarons
    return result

print(solution())