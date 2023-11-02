def solution():
    # Calculate the total number of marbles
    total_marbles = 12 + 28  

    # Calculate how many marbles each person will take away
    taken_away = (1/4) * total_marbles  

    # Calculate the number of marbles remaining in the pile
    remaining_marbles = total_marbles - (2 * taken_away)  

    result = remaining_marbles
    return result

print(solution())