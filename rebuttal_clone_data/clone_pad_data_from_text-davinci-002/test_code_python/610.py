def solution():
    percent_eaten_with_forks = 68
    total_pies = 2000
    pies_not_eaten_with_forks = total_pies * (1 - (percent_eaten_with_forks / 100))
    result = pies_not_eaten_with_forks
    return result

print(solution())