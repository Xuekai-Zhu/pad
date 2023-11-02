def solution():
    # Find the total number of marbles Atticus and Jensen have combined
    marbles_atticus = 4
    marbles_jensen = marbles_atticus * 2
    total_marbles_a_j = marbles_atticus + marbles_jensen

    # Find the number of marbles Cruz has
    total_marbles_a_j_c = 60 / 3
    marbles_cruz = total_marbles_a_j_c - total_marbles_a_j
    result = marbles_cruz
    return result

print(solution())