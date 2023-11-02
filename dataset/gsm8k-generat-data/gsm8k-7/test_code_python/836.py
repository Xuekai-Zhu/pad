def solution():
    num_flips = 211
    num_heads = 65

    # Calculate the number of tails
    num_tails = num_flips - num_heads

    # Calculate the difference between the number of tails and the number of heads
    diff = num_tails - num_heads
    result = diff
    return result

print(solution())