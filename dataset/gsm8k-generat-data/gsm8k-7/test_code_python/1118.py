def solution():
    phil_wins = 12
    charlie_wins = phil_wins - 3
    dana_wins = charlie_wins + 2
    perry_wins = dana_wins + 5

    diff = perry_wins - phil_wins
    result = diff
    return result

print(solution())