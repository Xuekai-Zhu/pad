def solution():
    """Amanda needs 12 more marbles to have twice as many marbles as Katrina, and Mabel has 5 times as many marbles as Katrina. If Mabel has 85 marbles, how many more marbles does Mabel have than Amanda?"""
    # Determine the number of marbles Katrina has
    katrina_marbles = 85 / 5
    # Determine the number of marbles Amanda has
    amanda_marbles = (katrina_marbles * 2) - 12
    # Determine the number of marbles Mabel has more than Amanda
    mabel_difference = 85 - amanda_marbles
    result = mabel_difference
    return result

print(solution())