def solution():
    """Out of the 500 marbles that Cindy had, she gave her four friends 80 marbles each. What's four times the number of marbles she has remaining?"""
    total_marbles = 500
    marbles_given_away = 80 * 4
    remaining_marbles = total_marbles - marbles_given_away
    result = remaining_marbles * 4
    return result

print(solution())