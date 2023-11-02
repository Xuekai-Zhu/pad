def solution():
    pink_marbles = 13  # Katie has 13 pink marbles
    orange_marbles = pink_marbles - 9  # Katie has 9 fewer orange marbles than pink marbles
    purple_marbles = 4 * orange_marbles  # Katie has 4 times as many purple marbles as orange marbles

    # Calculate the total number of marbles Katie has in all
    total_marbles = pink_marbles + orange_marbles + purple_marbles
    result = total_marbles
    return result

print(solution())