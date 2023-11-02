def solution():
    # Start with 40 pairs of socks
    num_pairs = 40

    # Lose 4 pairs at the laundromat
    num_pairs -= 4

    # Donate two-thirds of the remaining pairs
    num_pairs *= 1/3

    # Add 10 new pairs and 3 gift pairs
    num_pairs += 10 + 3

    result = num_pairs
    return result

print(solution())