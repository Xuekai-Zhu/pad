def solution():
    num_pink_marbles = 13
    num_orange_marbles = num_pink_marbles - 9
    num_purple_marbles = num_orange_marbles * 4

    # Calculate the total number of marbles that Katie has in all
    total_marbles = num_pink_marbles + num_orange_marbles + num_purple_marbles
    result = total_marbles
    return result

print(solution())