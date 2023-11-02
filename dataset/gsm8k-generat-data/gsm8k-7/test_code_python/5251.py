def solution():
    # Let N be the original number of pieces of cake
    # Guests ate half, so N/2 pieces were left
    leftovers = N/2

    # Donna shared half of the leftovers, so she had 1/4 of the original cake left
    leftovers /= 2

    # Donna ate 1 piece, so there were (2 * 1) = 2 pieces left
    # Therefore, there were (2 + 1) = 3 pieces left before Donna ate her midnight snack
    leftovers += 3

    # Twice as many pieces as Donna's snack were left, so there were (2 * 1) = 2 pieces left
    leftovers /= 2

    # Total number of pieces of cake is the sum of all the pieces (eaten, shared, and left)
    total_pieces = N + leftovers + 3 + 2

    return total_pieces

print(solution())