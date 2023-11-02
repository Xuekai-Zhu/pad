def solution():
    # Calculate the total number of rounds needed
    total_rounds = 110 // (2 + 3)

    # If there are leftover buckets, add another round
    if 110 % (2 + 3) != 0:
        total_rounds += 1

    result = total_rounds
    return result

print(solution())