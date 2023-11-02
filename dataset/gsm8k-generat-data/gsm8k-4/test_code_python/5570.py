def solution():
    """Lowry sells bonsai. A small bonsai costs $30 and a big bonsai costs $20. If he sold 3 small bonsai and 5 big bonsai, how much did he earn?"""
    # Define the cost of a small and big bonsai
    small_bonsai_cost = 30
    big_bonsai_cost = 20

    # Calculate the total earnings from selling small and big bonsai
    total_small_bonsai_earnings = 3 * small_bonsai_cost
    total_big_bonsai_earnings = 5 * big_bonsai_cost

    # Calculate the total earnings from selling all bonsai
    total_earnings = total_small_bonsai_earnings + total_big_bonsai_earnings

    # return the result
    result = total_earnings
    return result

print(solution())