def solution():
    # Define the number of flips and heads
    num_flips = 211
    num_heads = 65

    # Calculate the number of tails
    num_tails = num_flips - num_heads

    # Calculate the difference between tails and heads
    diff_tails_heads = num_tails - num_heads
    result = diff_tails_heads
    return result

print(solution())