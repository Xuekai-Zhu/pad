def solution():
    """Three times the sum of marbles that Atticus, Jensen, and Cruz have is equal to 60. If Atticus has half as many marbles as Jensen, and Atticus has 4 marbles, how many marbles does Cruz have?"""
    atticus_marbles = 4
    jensen_marbles = atticus_marbles * 2
    sum_of_marbles = atticus_marbles + jensen_marbles + cruz_marbles
    total = sum_of_marbles * 3
    cruz_marbles = (total - (atticus_marbles + jensen_marbles)) / 3
    result = cruz_marbles
    return result

print(solution())