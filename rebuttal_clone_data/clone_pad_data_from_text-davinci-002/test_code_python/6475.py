def solution():
    sum_of_marbles = 60
    atticus_marbles = 4
    jensen_marbles = atticus_marbles * 2
    cruz_marbles = sum_of_marbles - (atticus_marbles + jensen_marbles)
    result = cruz_marbles
    return result

print(solution())