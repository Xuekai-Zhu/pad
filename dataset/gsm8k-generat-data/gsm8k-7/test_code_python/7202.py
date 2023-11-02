def solution():
    chris_marbles = 12
    ryan_marbles = 28

    # Calculate the total number of marbles in the pile
    total_marbles = chris_marbles + ryan_marbles

    # Calculate the number of marbles taken away by each person
    taken_away = total_marbles * 0.25

    # Calculate the number of marbles remaining in the pile
    remaining_marbles = total_marbles - (2 * taken_away)
    result = remaining_marbles
    return result

print(solution())