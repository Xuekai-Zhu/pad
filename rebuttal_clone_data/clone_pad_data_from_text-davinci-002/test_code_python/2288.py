def solution():
    total_marbles = 600
    brittany_marbles = total_marbles / 3
    alex_marbles = total_marbles / 5
    jamy_marbles = total_marbles / 7
    alex_new_marbles = (brittany_marbles / 2) + alex_marbles
    result = alex_new_marbles
    return result

print(solution())