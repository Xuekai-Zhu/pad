def solution():
    """Emma bought 3 dozens of macarons in addition to her 10 pieces of macarons for a party. If 15 pieces of macarons are left over, how many pieces of macarons were eaten?"""
    # Define the number of macarons per dozen
    MACARONS_PER_DOZEN = 12

    # Calculate the total number of macarons
    total_macarons = 3 * MACARONS_PER_DOZEN + 10

    # Calculate the number of macarons eaten
    eaten_macarons = total_macarons - 15

    result = eaten_macarons
    return result

print(solution())