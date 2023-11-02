def solution():
    bettys_marbles = 60
    stuarts_percent = 40
    stuarts_marbles = bettys_marbles * (stuarts_percent / 100)
    total_marbles = bettys_marbles + stuarts_marbles
    result = total_marbles / 2
    return result

print(solution())