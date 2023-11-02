def solution():
    """Amanda needs 12 more marbles to have twice as many marbles as Katrina, and Mabel has 5 times as many marbles as Katrina. If Mabel has 85 marbles, how many more marbles does Mabel have than Amanda?"""
    katrina_marbles = 12 / 2
    mabel_marbles = katrina_marbles * 5
    amanda_marbles = katrina_marbles + 12
    mabel_total = mabel_marbles + 85
    difference = mabel_total - amanda_marbles
    result = difference
    return result

print(solution())