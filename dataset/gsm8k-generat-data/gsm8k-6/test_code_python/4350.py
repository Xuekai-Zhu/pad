def solution():
    # Calculate the number of marbles Cindy has remaining after giving her four friends 80 each
    remaining_marbles = 500 - (80 * 4)

    # Calculate four times the remaining number of marbles
    result = 4 * remaining_marbles
    return result

print(solution())