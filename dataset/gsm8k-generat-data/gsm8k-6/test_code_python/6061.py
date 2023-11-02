def solution():
    # Find the total number of blue marbles
    blue_marbles = 3 * 14

    # Find the total number of yellow marbles
    yellow_marbles = 85 - 14 - blue_marbles

    result = yellow_marbles
    return result

print(solution())