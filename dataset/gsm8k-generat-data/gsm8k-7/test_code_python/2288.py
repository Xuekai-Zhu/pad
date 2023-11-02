def solution():
    total_marbles = 600
    ratio = [3, 5, 7]

    # calculate the total parts in the ratio
    total_parts = sum(ratio)

    # calculate the number of marbles for each person based on the ratio
    brittany_marbles = (ratio[0] / total_parts) * total_marbles
    alex_marbles = (ratio[1] / total_parts) * total_marbles
    jamy_marbles = (ratio[2] / total_parts) * total_marbles

    # Brittany gives half of her marbles to Alex
    alex_marbles += (0.5 * brittany_marbles)

    # calculate the total number of marbles Alex has
    total_alex_marbles = alex_marbles
    result = total_alex_marbles
    return result

print(solution())