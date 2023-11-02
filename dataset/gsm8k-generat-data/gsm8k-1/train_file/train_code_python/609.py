def solution():
    """68% of all pies are eaten with forks. If there are 2000 pies of all kinds, how many of the pies are not eaten with forks?"""
    total_pies = 2000
    percent_with_forks = 68
    pies_with_forks = total_pies * (percent_with_forks/100)
    pies_without_forks = total_pies - pies_with_forks
    result = pies_without_forks
    return result

print(solution())