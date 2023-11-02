def solution():
    """Amanda needs 12 more marbles to have twice as many marbles as Katrina, and Mabel has 5 times as many marbles as Katrina. If Mabel has 85 marbles, how many more marbles does Mabel have than Amanda?"""
    mabel_marbles = 85
    katrina_marbles = mabel_marbles / 5
    amanda_twice_katrina = katrina_marbles * 2
    amanda_marbles = amanda_twice_katrina - 12
    difference = mabel_marbles - amanda_marbles
    result = difference
    return result

print(solution())