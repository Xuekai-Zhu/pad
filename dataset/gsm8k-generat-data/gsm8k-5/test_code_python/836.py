def solution():
    total_flips = 211  # The solver flipped the coin 211 times
    heads = 65  # The solver got 65 heads

    # Calculate the number of tails
    tails = total_flips - heads

    # Calculate the difference between the number of tails and heads
    difference = tails - heads
    result = difference
    return result

print(solution())