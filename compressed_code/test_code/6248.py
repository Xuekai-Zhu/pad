def solution():
    
    total_pies = 2000
    percent_with_forks = 68
    pies_with_forks = total_pies * (percent_with_forks/100)
    pies_without_forks = total_pies - pies_with_forks
    result = pies_without_forks
    return result

print(solution())