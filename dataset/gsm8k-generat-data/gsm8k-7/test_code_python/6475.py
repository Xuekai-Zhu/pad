def solution():
    atticus_marbles = 4
    jensen_marbles = atticus_marbles * 2
    sum_marbles = (atticus_marbles + jensen_marbles + cruz_marbles)
    equation = 3 * sum_marbles
    if equation == 60:
        cruz_marbles = (60 / 3 - atticus_marbles - jensen_marbles)
        result = cruz_marbles
    else:
        result = "Invalid equation"
    return result

print(solution())