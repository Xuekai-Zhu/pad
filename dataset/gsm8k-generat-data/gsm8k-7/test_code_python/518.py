def solution():
    selma_marbles = 50
    total_marbles = selma_marbles - 5  # total of Elliot and Merill's marbles
    merill_marbles = 2 * (total_marbles / 3)  # Merill has twice as many marbles as Elliot
    result = merill_marbles
    return result

print(solution())