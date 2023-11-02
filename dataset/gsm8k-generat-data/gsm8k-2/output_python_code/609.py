def solution():
    """68% of all pies are eaten with forks. If there are 2000 pies of all kinds, how many of the pies are not eaten with forks?"""
    total_pies = 2000
    fork_pies = total_pies * 0.68
    non_fork_pies = total_pies - fork_pies
    result = non_fork_pies
    return result

print(solution())