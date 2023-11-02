def solution():
    """Lowry sells bonsai. A small bonsai costs $30 and a big bonsai costs $20. If he sold 3 small bonsai and 5 big bonsai, how much did he earn?"""
    # Define the prices of the different bonsai
    SMALL_PRICE = 30
    BIG_PRICE = 20

    # Define the number of small and big bonsai sold
    small_bonsai = 3
    big_bonsai = 5

    # Calculate the total earnings
    total_earnings = (small_bonsai * SMALL_PRICE) + (big_bonsai * BIG_PRICE)

    # Display the total earnings
    result = total_earnings
    return result

print(solution())