def solution():
    # Find the total number of parts in the ratio
    total_parts = 3 + 5 + 7

    # Find the number of marbles in one part of the ratio
    one_part = 600 / total_parts

    # Find the number of marbles Brittany has
    brittany_marbles = 3 * one_part

    # Find the number of marbles Alex has after Brittany gives him half of hers
    alex_marbles = 5 * one_part + (1/2) * brittany_marbles

    result = alex_marbles
    return result

print(solution())